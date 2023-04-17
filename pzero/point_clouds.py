from copy import deepcopy

from pyvista.core.filters import _update_alg
from vtkmodules.util import numpy_support
from vtkmodules.vtkCommonCore import vtkIdTypeArray
from vtkmodules.vtkCommonDataModel import vtkDataObject, vtkImplicitSelectionLoop, vtkPolyData, vtkSelectionNode, \
    vtkSelection, vtkPlane
from vtkmodules.vtkFiltersCore import vtkThreshold, vtkAppendPolyData, vtkThresholdPoints, vtkDelaunay2D, \
    vtkMassProperties
from vtkmodules.vtkFiltersExtraction import vtkExtractGeometry, vtkExtractSelection
from vtkmodules.vtkFiltersPoints import vtkEuclideanClusterExtraction, vtkRadiusOutlierRemoval, vtkProjectPointsToPlane

from .dom_collection import DomCollection
from .entities_factory import PCDom, TriSurf, Attitude
from .geological_collection import GeologicalCollection
from .helper_dialogs import multiple_input_dialog
from .helper_functions import best_fitting_plane
from .helper_widgets import Scissors

from numpy import max as np_max
from numpy import random as np_random
from numpy import repeat as np_repeat
from numpy import pi as np_pi
from numpy import arctan2 as np_arctan2
from numpy import arcsin as np_arcsin
from numpy import zeros_like as np_zeros_like
from numpy import std as np_std

from uuid import uuid4


def normals2dd(self):
    if len(self.selected_uids) == 0:
        print('No entities selected, make sure to have the right tab open')
        return
    for uid in self.selected_uids:
        vtk_obj = self.parent.dom_coll.get_uid_vtk_obj(uid)
        prop_keys = vtk_obj.point_data_keys
        if 'Normals' not in prop_keys:
            print('Normal data not present. Import or create normal data to proceed')
        else:
            dip = vtk_obj.points_map_dip
            dip_az = vtk_obj.points_map_dip_azimuth

            # print(np.rad2deg(dir))
            vtk_obj.init_point_data('dip', 1)
            vtk_obj.init_point_data('dip direction', 1)

            vtk_obj.set_point_data('dip', dip)
            vtk_obj.set_point_data('dip direction', dip_az)

            self.parent.dom_coll.replace_vtk(uid, vtk_obj)


def extract_id(vtk_obj, ids):

    selection_node = vtkSelectionNode()
    selection_node.SetFieldType(vtkSelectionNode.POINT)
    selection_node.SetContentType(vtkSelectionNode.INDICES)
    selection_node.SetSelectionList(ids)

    selection = vtkSelection()
    selection.AddNode(selection_node)

    extract_selection = vtkExtractSelection()
    extract_selection.SetInputData(0, vtk_obj)
    extract_selection.SetInputData(1, selection)
    extract_selection.Update()

    vtk_ps_subset = PCDom()
    vtk_ps_subset.ShallowCopy(extract_selection.GetOutput())
    vtk_ps_subset.remove_point_data('vtkOriginalPointIds')
    vtk_ps_subset.Modified()

    return vtk_ps_subset


def cut_pc(self):
    def end_digitize(event):
        self.plotter.untrack_click_position()
        uid = self.selected_uids[0]
        vtk_obj = self.parent.dom_coll.get_uid_vtk_obj(uid)
        # Signal called to end the digitization of a trace. It returns a new polydata
        loop = vtkImplicitSelectionLoop()
        loop.SetLoop(scissors.GetContourRepresentation().GetContourRepresentationAsPolyData().GetPoints())

        clip_out, clip_in = extract_pc(vtk_obj, loop)
        entity_dict = deepcopy(self.parent.dom_coll.dom_entity_dict)
        # print(entity_dict)
        entity_dict['name'] = self.parent.dom_coll.get_uid_name(uid) + '_cut_in'
        entity_dict['vtk_obj'] = clip_in
        entity_dict['dom_type'] = 'PCDom'
        entity_dict['properties_names'] = self.parent.dom_coll.get_uid_properties_names(uid)
        entity_dict['dom_type'] = 'PCDom'
        entity_dict['properties_components'] = self.parent.dom_coll.get_uid_properties_components(uid)
        entity_dict['vtk_obj'] = clip_in
        self.parent.dom_coll.add_entity_from_dict(entity_dict)

        entity_dict = deepcopy(self.parent.dom_coll.dom_entity_dict)
        # print(entity_dict)
        entity_dict['name'] = self.parent.dom_coll.get_uid_name(uid) + '_cut_out'
        entity_dict['vtk_obj'] = clip_out
        entity_dict['dom_type'] = 'PCDom'
        entity_dict['properties_names'] = self.parent.dom_coll.get_uid_properties_names(uid)
        entity_dict['dom_type'] = 'PCDom'
        entity_dict['properties_components'] = self.parent.dom_coll.get_uid_properties_components(uid)
        entity_dict['vtk_obj'] = clip_out

        self.parent.dom_coll.add_entity_from_dict(entity_dict)

        scissors.EnabledOff()
        self.enable_actions()
        self.clear_selection()

    if not self.selected_uids:
        print(" -- No input data selected -- ")
        return
    """Freeze QT interface"""
    self.disable_actions()

    """Getting the values that have been typed by the user through the widget"""

    scissors = Scissors(self)
    scissors.EnabledOn()
    self.plotter.track_click_position(side='right', callback=end_digitize)


def decimate_pc(vtk_obj, fac):
    dec_fac = int(vtk_obj.GetNumberOfPoints() * fac)
    random = np_random.choice(vtk_obj.GetNumberOfPoints(), dec_fac)

    ids = vtkIdTypeArray()

    for i in random:
        ids.InsertNextValue(i)

    selection = extract_id(vtk_obj, ids)

    return selection


def extract_pc(vtk_obj, implicit_func):
    clip = vtkExtractGeometry()
    clip.SetInputData(vtk_obj)
    clip.SetImplicitFunction(implicit_func)
    clip.ExtractInsideOn()
    clip.Update()

    clip_in = PCDom()
    clip_in.ShallowCopy(clip.GetOutput())
    clip.ExtractInsideOff()
    clip.Modified()
    clip.Update()
    clip_out = PCDom()
    clip_out.ShallowCopy(clip.GetOutput())

    return clip_out, clip_in


def segment_pc(self):

    if len(self.selected_uids) == 0:
        print('No entities selected, make sure to have the right tab open')
        return
    else:
        uid = self.selected_uids[0]

    vtk_obj = self.parent.dom_coll.get_uid_vtk_obj(uid)

    if isinstance(vtk_obj, PCDom):
        if 'dip direction' not in self.parent.dom_coll.get_uid_properties_names(uid):
            print(
                'dip directio/dip data not present in the dataset. Calculate from Normals using the specific function.')
            return
        input_dict = {'name': ['Name result: ', 'segmented_'],
                      'dd1': ['Dip direction lower threshold: ', 0],
                      'dd2': ['Dip direction upper threshold: ', 10],
                      'd1': ['Dip lower threshold: ', 0],
                      'd2': ['Dip upper threshold: ', 10],
                      'rad': ['Search radius: ', 0.0],
                      'nn': ['Minimum number of neighbors: ', 15]}
        dialog = multiple_input_dialog(title='Segmentation filter', input_dict=input_dict)

        # print(dialog)

        vtk_obj.GetPointData().SetActiveScalars('dip direction')
        connectivity_filter_dd = vtkEuclideanClusterExtraction()
        connectivity_filter_dd.SetInputData(vtk_obj)
        connectivity_filter_dd.SetRadius(dialog['rad'])
        connectivity_filter_dd.SetExtractionModeToAllClusters()
        connectivity_filter_dd.ScalarConnectivityOn()
        connectivity_filter_dd.SetScalarRange(dialog['dd1'], dialog['dd2'])
        _update_alg(connectivity_filter_dd, True, 'Segmenting on dip directions')
        f1 = connectivity_filter_dd.GetOutput()
        # print(f1)
        f1.GetPointData().SetActiveScalars('dip')
        # print(f1.GetNumberOfPoints())
        #
        connectivity_filter_dip = vtkEuclideanClusterExtraction()
        connectivity_filter_dip.SetInputData(f1)
        connectivity_filter_dip.SetRadius(dialog['rad'])
        connectivity_filter_dip.SetExtractionModeToAllClusters()
        connectivity_filter_dip.ColorClustersOn()
        connectivity_filter_dip.ScalarConnectivityOn()
        connectivity_filter_dip.SetScalarRange(dialog['d1'], dialog['d2'])

        _update_alg(connectivity_filter_dip, True, 'Segmenting dips')

        n_clusters = connectivity_filter_dip.GetNumberOfExtractedClusters()

        # print(n_clusters)

        # r = vtkRadiusOutlierRemoval()
        # r.SetInputData(connectivity_filter_dip.GetOutput())
        # r.SetRadius(dialog['rad'])
        # r.SetNumberOfNeighbors(dialog['nn'])
        # r.GenerateOutliersOff()
        #
        # _update_alg(r, True, 'Cleaning pc')
        pc = connectivity_filter_dip.GetOutput()
        pc.GetPointData().SetActiveScalars('ClusterId')
        appender_pc = vtkAppendPolyData()
        for i in range(n_clusters):
            print(f'{i}/{n_clusters}', end='\r')

            thresh = vtkThresholdPoints()

            thresh.SetInputData(pc)
            thresh.ThresholdBetween(i, i)

            thresh.Update()
            if thresh.GetOutput().GetNumberOfPoints() > dialog['nn']:
                appender_pc.AddInputData(thresh.GetOutput())
        appender_pc.Update()

        seg_pc = PCDom()
        seg_pc.ShallowCopy(appender_pc.GetOutput())
        seg_pc.generate_cells()
        properties_name = seg_pc.point_data_keys
        properties_components = [seg_pc.get_point_data_shape(i)[1] for i in properties_name]

        curr_obj_dict = deepcopy(DomCollection.dom_entity_dict)
        curr_obj_dict['uid'] = str(uuid4())
        curr_obj_dict['name'] = f'pc_{dialog["name"]}'
        curr_obj_dict['dom_type'] = "PCDom"
        curr_obj_dict['properties_names'] = properties_name
        curr_obj_dict['properties_components'] = properties_components
        curr_obj_dict['vtk_obj'] = seg_pc
        """Add to entity collection."""
        self.parent.dom_coll.add_entity_from_dict(entity_dict=curr_obj_dict)

        del f1
        del seg_pc
        del properties_name
        del properties_components

    else:
        print('Entity not point cloud or multiple entities visible')


def facets_pc(self):
    if len(self.selected_uids) == 0:
        print('No entities selected, make sure to have the right tab open')
        return
    else:
        uid = self.selected_uids[0]

    vtk_obj = self.parent.dom_coll.get_uid_vtk_obj(uid)
    name = self.parent.dom_coll.get_uid_name(uid)
    appender = vtkAppendPolyData()
    max_region = np_max(vtk_obj.get_point_data('ClusterId'))
    vtk_obj.GetPointData().SetActiveScalars('ClusterId')
    for i in range(max_region):
        print(f'{i}/{max_region}', end='\r')

        thresh = vtkThresholdPoints()

        thresh.SetInputData(vtk_obj)
        thresh.ThresholdBetween(i, i)

        thresh.Update()
        points = numpy_support.vtk_to_numpy(thresh.GetOutput().GetPoints().GetData())
        n_points = thresh.GetOutput().GetNumberOfPoints()
        if n_points > 0:
            c, n = best_fitting_plane(points)
            if n[2] >= 0:
                n *= -1
            dd = np_repeat((np_arctan2(n[0], n[1]) * 180 / np_pi - 180) % 360, n_points)
            d = np_repeat(90 - np_arcsin(-n[2]) * 180 / np_pi, n_points)

            facet = TriSurf()
            plane_proj = vtkProjectPointsToPlane()
            plane_proj.SetInputData(thresh.GetOutput())
            plane_proj.SetProjectionTypeToBestFitPlane()

            delaunay = vtkDelaunay2D()
            delaunay.SetInputConnection(plane_proj.GetOutputPort())
            delaunay.SetProjectionPlaneMode(2)
            delaunay.Update()
            facet.ShallowCopy(delaunay.GetOutput())

            mass = vtkMassProperties()
            mass.SetInputData(facet)
            area = np_repeat(mass.GetSurfaceArea(), n_points)
            facet.remove_point_data('Normals')
            facet.set_point_data('dip direction', dd)
            facet.set_point_data('dip', d)
            facet.set_point_data('area', area)
            appender.AddInputData(facet)

    appender.Update()

    facets = TriSurf()
    facets.ShallowCopy(appender.GetOutput())
    properties_name = facets.point_data_keys
    properties_components = [facets.get_point_data_shape(i)[1] for i in properties_name]

    curr_obj_dict = deepcopy(GeologicalCollection.geological_entity_dict)
    curr_obj_dict['uid'] = str(uuid4())
    curr_obj_dict['name'] = f'{name}facets'
    curr_obj_dict['geological_type'] = 'undef'
    curr_obj_dict['topological_type'] = "TriSurf"
    curr_obj_dict['geological_feature'] = name
    curr_obj_dict['properties_names'] = properties_name
    curr_obj_dict['properties_components'] = properties_components
    curr_obj_dict['vtk_obj'] = facets
    """Add to entity collection."""
    self.parent.geol_coll.add_entity_from_dict(entity_dict=curr_obj_dict)


def calibration_pc(vtk_objs):

    n_points = np_zeros_like(len(vtk_objs))

    normals_var = np_zeros_like(len(vtk_objs))
    for i, vtk_obj in enumerate(vtk_objs):
        points = vtk_obj.points
        normals = numpy_support.vtk_to_numpy(vtk_obj.GetPointData().GetScalars('Normals'))
        n_points[i] = vtk_obj.GetNumberOfPoints()
        normals_var[i] = np_std(normals, axis=0)

        c, n = best_fitting_plane(points)
        if n[2] >= 0:
            n *= -1

        plane2 = vtkPlane()
        plane2.SetOrigin(c)
        plane2.SetNormal(n)

        distances = []

        for point in points:
            distances.append(plane2.DistanceToPlane(point))

        # Calculate distance from fitted plane -> estimate of roughness
        # Calculate mean distance from fitted plane
        # Calculate vector normal direction variation (over the 3 components) ->SRF
        # Calculate surface density for given facet and volume density (how?)
        # Calculate loading scores.
        # Calculate N of neighbours


def auto_pick(self):

    if len(self.selected_uids) == 0:
        print('No entities selected, make sure to have the right tab open')
        return
    else:
        uid = self.selected_uids[0]

    vtk_obj = self.parent.dom_coll.get_uid_vtk_obj(uid)
    name = self.parent.dom_coll.get_uid_name(uid)
    appender = vtkAppendPolyData()
    max_region = np_max(vtk_obj.get_point_data('ClusterId'))
    vtk_obj.GetPointData().SetActiveScalars('ClusterId')
    for i in range(max_region):
        print(f'{i}/{max_region}', end='\r')
        thresh = vtkThresholdPoints()

        thresh.SetInputData(vtk_obj)
        thresh.ThresholdBetween(i, i)

        thresh.Update()

        points = numpy_support.vtk_to_numpy(thresh.GetOutput().GetPoints().GetData())
        # print(points)
        if thresh.GetOutput().GetNumberOfPoints() > 0:
            # print(thresh.GetOutput())
            c, n = best_fitting_plane(points)
            # n = np.mean(numpy_support.vtk_to_numpy(thresh.GetOutput().GetPointData().GetArray('Normals')),axis=0)
            # c = np.mean(points,axis=0)
            if n[2] >= 0:
                n *= -1
            # plane = pv.Plane(center = c, direction= n)
            att_point = Attitude()
            att_point.append_point(point_vector=c)
            att_point.auto_cells()
            att_point.set_point_data(data_key='Normals', attribute_matrix=n)
            appender.AddInputData(att_point)

    appender.Update()

    points = Attitude()
    points.ShallowCopy(appender.GetOutput())
    properties_name = points.point_data_keys
    properties_components = [points.get_point_data_shape(i)[1] for i in properties_name]

    curr_obj_dict = deepcopy(GeologicalCollection.geological_entity_dict)
    curr_obj_dict['uid'] = str(uuid4())
    curr_obj_dict['name'] = f'{name}auto_pick'
    curr_obj_dict['geological_type'] = 'undef'
    curr_obj_dict['topological_type'] = "VertexSet"
    curr_obj_dict['geological_feature'] = name
    curr_obj_dict['properties_names'] = properties_name
    curr_obj_dict['properties_components'] = properties_components
    curr_obj_dict['vtk_obj'] = points
    """Add to entity collection."""
    self.parent.geol_coll.add_entity_from_dict(entity_dict=curr_obj_dict)




'''[Gabriele] PC Filters ----------------------------------------------------'''


def thresh_filt(self):

    uid = self.actors_df.loc[self.actors_df['show'] == True, 'uid'].values[0]
    vtk_obj = self.parent.dom_coll.get_uid_vtk_obj(uid)
    if isinstance(vtk_obj,PCDom):
        input_dict = {'prop_name': ['Select property name: ', vtk_obj.properties_names], 'l_t': ['Lower threshold: ', 0], 'u_t': ['Upper threshold: ', 10]}
        dialog = multiple_input_dialog(title='Threshold filter', input_dict=input_dict)

        thresh = vtkThreshold()
        thresh.SetInputData(vtk_obj)
        thresh.SetInputArrayToProcess(0, 0, 0, vtkDataObject.FIELD_ASSOCIATION_POINTS, dialog['prop_name'])
        thresh.SetLowerThreshold(float(dialog['l_t']))
        thresh.SetUpperThreshold(float(dialog['u_t']))
        thresh.Update()
        out = PCDom()
        out.ShallowCopy(thresh.GetOutput())
        out.generate_cells()
        # out.plot()
        # self.parent.dom_coll.replace_vtk(uid[0],out)
        entity_dict = deepcopy(self.parent.dom_coll.dom_entity_dict)
        # print(entity_dict)
        entity_dict['name'] = self.parent.dom_coll.get_uid_name(uid) + '_thresh_'+str(dialog['l_t'])+'_'+str(dialog['u_t'])
        entity_dict['vtk_obj'] = out
        entity_dict['dom_type'] = 'PCDom'
        entity_dict['properties_names'] = self.parent.dom_coll.get_uid_properties_names(uid)
        entity_dict['dom_type'] = 'PCDom'
        entity_dict['properties_components'] = self.parent.dom_coll.get_uid_properties_components(uid)
        entity_dict['vtk_obj'] = out
        self.parent.dom_coll.add_entity_from_dict(entity_dict)
        del out
        del thresh
    else:
        print('Entity not point cloud or multiple entities visible')


def radial_filt(self):
    ...


def surf_den_filt(self):
    ...


def rough_filt(self):
    ...


def curv_filt(self):
    ...


def col_filt(self):
    ...