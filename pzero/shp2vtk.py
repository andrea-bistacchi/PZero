"""shp2vtk.py
PZero© Andrea Bistacchi"""

from copy import deepcopy

from matplotlib.text import Annotation
from sqlalchemy import column
from .entities_factory import Fritti, PolyLine, VertexSet, Attitude
from numpy import array as np_array
from numpy import shape as np_shape
from numpy import zeros as np_zeros
from numpy import column_stack as np_column_stack
from pandas import Series as pd_series
from geopandas import read_file as gpd_read_file
from vtk import vtkAppendPolyData
from .geological_collection import GeologicalCollection
from .fluid_collection import FluidsCollection
from .frittura_collection import FrittoMistoCollection
from .two_d_lines import left_right
from shapely import affinity
from shapely.geometry import asLineString, LineString, Point, asPoint, MultiLineString
from shapely.ops import split, snap

from .orientation_analysis import dip_directions2normals
"""Importer for SHP files and other GIS formats, to be improved IN THE FUTURE.
Known bugs for multi-part polylines.
Points not handled correctly."""


# 'name': "undef"  ###
# 'topological_type': "undef"  ###
# 'geological_type': "undef"  ###
# 'geological_feature': "undef"  ###
# 'scenario': "undef"
# 'properties_names': []
# 'properties_components': []
# 'x_section': ""
# 'vtk_obj': None

def shp2vtk(self=None, in_file_name=None,collection=None):
    """Import and add a points and polylines from shape files as VertexSet and PolyLine entities.
    <self> is the calling ProjectWindow() instance."""
    # try:
    """Read shape file into a GeoPandas dataframe. Each row is an entity with geometry stored in the geometry column in shapely format."""
    gdf = gpd_read_file(in_file_name)
    # print("geometry type: ", gdf.geom_type[0])
    # print("CRS:\n", gdf.crs)
    # if False in gdf.is_valid[:]:
    #     print("Not valid geometries found - aborting.")
    #     return
    # if True in gdf.is_empty[:]:
    #     print("Empty geometries found - aborting.")
    #     return
    column_names = list(gdf.columns)
    # print("Column names of GeoDataframe: ", list(gdf.columns))
    # print("GeoDataframe:\n", gdf)
    # [Gabriele] This is horroble, we should rewrite to accept 
    # different types of collection without repeating the code 
    if collection == 'Geology':
        if (gdf.geom_type[0] == "LineString") or (gdf.geom_type[0] == "MultiLineString"):
            for row in range(gdf.shape[0]):
                # print("____ROW: ", row)
                # print("geometry type: ", gdf.geom_type[row])
                curr_obj_dict = deepcopy(GeologicalCollection.geological_entity_dict)
                # if gdf.is_valid[row] and not gdf.is_empty[row]:
                # try:
                if "name" in column_names:
                    curr_obj_dict["name"] = gdf.loc[row, "name"]
                if "geological_type" in column_names:
                    curr_obj_dict["geological_type"] = gdf.loc[row, "geological_type"]
                if "geo_type" in column_names:
                    curr_obj_dict["geological_type"] = gdf.loc[row, "geo_type"]
                if "geological_feature" in column_names:
                    curr_obj_dict["geological_feature"] = gdf.loc[row, "geological_feature"]
                if "geo_feat" in column_names:
                    curr_obj_dict["geological_feature"] = gdf.loc[row, "geo_feat"]
                if "scenario" in column_names:
                    curr_obj_dict["scenario"] = gdf.loc[row, "scenario"]
                curr_obj_dict["topological_type"] = "PolyLine"
                curr_obj_dict["vtk_obj"] = PolyLine()
                if gdf.geom_type[row] == "LineString":
                    outXYZ = np_array(gdf.loc[row].geometry)
                    # print("outXYZ:\n", outXYZ)
                    if np_shape(outXYZ)[1] == 2:
                        outZ = np_zeros((np_shape(outXYZ)[0], 1))
                        # print("outZ:\n", outZ)
                        outXYZ = np_column_stack((outXYZ, outZ))
                    # print("outXYZ:\n", outXYZ)
                    curr_obj_dict["vtk_obj"].points = outXYZ
                    curr_obj_dict["vtk_obj"].auto_cells()
                elif gdf.geom_type[row] == "MultiLineString":
                    outXYZ_list = np_array(gdf.loc[row].geometry)
                    vtkappend = vtkAppendPolyData()
                    for outXYZ in outXYZ_list:
                        temp_vtk = PolyLine()
                        # print("outXYZ:\n", outXYZ)
                        # print("np_shape(outXYZ):\n", np_shape(outXYZ))
                        if np_shape(outXYZ)[1] == 2:
                            outZ = np_zeros((np_shape(outXYZ)[0], 1))
                            # print("outZ:\n", outZ)
                            outXYZ = np_column_stack((outXYZ, outZ))
                        # print("outXYZ:\n", outXYZ)
                        temp_vtk.points = outXYZ
                        temp_vtk.auto_cells()
                        vtkappend.AddInputData(temp_vtk)
                    vtkappend.Update()
                    curr_obj_dict["vtk_obj"].ShallowCopy(vtkappend.GetOutput())
                """Create entity from the dictionary and run left_right."""
                if curr_obj_dict["vtk_obj"].points_number > 0:
                    output_uid = self.geol_coll.add_entity_from_dict(curr_obj_dict)
                else:
                    print("Empty object")
                # else:
                # except:
                #     print("Invalid object")
                del curr_obj_dict
        elif gdf.geom_type[0] == "Point":
            if "geo_feat" in column_names:
                gdf_index = gdf.set_index("geo_feat")
                feat_list = set(gdf_index.index)



                for i in feat_list:
                    curr_obj_dict = deepcopy(GeologicalCollection.geological_entity_dict)
                    if 'dip' in gdf.columns:
                        vtk_obj = Attitude()
                    else:
                        vtk_obj = VertexSet()

                    if "name" in column_names:
                        curr_obj_dict["name"] = pd_series(gdf_index.loc[i, "name"])[0]
                    if "geological_type" in column_names:
                        curr_obj_dict["geological_type"] = pd_series(gdf_index.loc[i, "geological_type"])[0]
                    if "geo_type" in column_names:
                        curr_obj_dict["geological_type"] = pd_series(gdf_index.loc[i, "geo_type"])[0]
                    if "geological_feature" in column_names:
                        curr_obj_dict["geological_feature"] = i
                    if "geo_feat" in column_names:
                        curr_obj_dict["geological_feature"] = i
                    if "scenario" in column_names:
                        curr_obj_dict["scenario"] = pd_series(gdf_index.loc[i, "scenario"])[0]

                    curr_obj_dict["topological_type"] = "VertexSet"
                    curr_obj_dict["vtk_obj"] = vtk_obj

                    gdf_index['coords'] = gdf_index.geometry.apply(lambda x: np_array(x)) # [Gabriele] add a coordinate column in the gdf_index dataframe
                    outXYZ = np_array([p for p in gdf_index.loc[i, 'coords']])

                    if outXYZ.ndim == 1:
                        outXYZ = outXYZ.reshape(-1,np_shape(outXYZ)[0])

                    if np_shape(outXYZ)[1] == 2:
                        outZ = np_zeros((np_shape(outXYZ)[0], 1))
                        # print("outZ:\n", outZ)
                        outXYZ = np_column_stack((outXYZ, outZ))


                    # print(np_shape(outXYZ))
                    curr_obj_dict["vtk_obj"].points = outXYZ

                    if 'dip_dir' in column_names:
                        dir = pd_series((gdf_index.loc[i, "dip_dir"]-90)%360)
                        curr_obj_dict["vtk_obj"].set_point_data('dir', dir.values)
                    if 'dir' in column_names:
                        curr_obj_dict["vtk_obj"].set_point_data('dir', pd_series(gdf_index.loc[i, "dir"]).values)
                    if 'dip':
                        curr_obj_dict["vtk_obj"].set_point_data('dip', pd_series(gdf_index.loc[i, "dip"]).values)
                    
                    if 'dip' in column_names and ('dir' in column_names or 'dip_dir' in column_names):
                        # print(type(curr_obj_dict["vtk_obj"].get_point_data('dip')))
                        normals = dip_directions2normals(curr_obj_dict["vtk_obj"].get_point_data('dip'), curr_obj_dict["vtk_obj"].get_point_data('dir'))
                        curr_obj_dict["vtk_obj"].set_point_data('Normals',normals)




                    if curr_obj_dict["vtk_obj"].points_number > 1:
                        curr_obj_dict["vtk_obj"].auto_cells()
                        # print(curr_obj_dict["vtk_obj"].point_data_keys)
                        properties_names = curr_obj_dict["vtk_obj"].point_data_keys
                        properties_components = [curr_obj_dict["vtk_obj"].get_point_data_shape(key)[1] for key in properties_names]
                        curr_obj_dict['properties_names'] = properties_names
                        curr_obj_dict['properties_components'] = properties_components
                        self.geol_coll.add_entity_from_dict(curr_obj_dict)
                        del curr_obj_dict
                    elif curr_obj_dict["vtk_obj"].points_number > 0:
                        curr_obj_dict["vtk_obj"].auto_cells()
                        # print(curr_obj_dict["vtk_obj"].point_data_keys)
                        properties_names = curr_obj_dict["vtk_obj"].point_data_keys
                        properties_components = [curr_obj_dict["vtk_obj"].get_point_data_shape(key)[1] for key in properties_names]
                        curr_obj_dict['properties_names'] = properties_names
                        curr_obj_dict['properties_components'] = properties_components
                        self.geol_coll.add_entity_from_dict(curr_obj_dict)
                        del curr_obj_dict
            else:
                print('Incomplete data. At least the geological_feature property must be present')
        else:
            print("Only Point and Line geometries can be imported - aborting.")
            return  # except:  #     self.TextTerminal.appendPlainText("SHP file not recognized ERROR.")
    elif collection == 'Fluid contacts':
        print(gdf.geom_type[0])
        if (gdf.geom_type[0] == "LineString") or (gdf.geom_type[0] == "MultiLineString"):
            for row in range(gdf.shape[0]):
                # print("____ROW: ", row)
                # print("geometry type: ", gdf.geom_type[row])
                curr_obj_dict = deepcopy(FluidsCollection.fluid_entity_dict)
                # if gdf.is_valid[row] and not gdf.is_empty[row]:
                # try:
                if "name" in column_names:
                    curr_obj_dict["name"] = gdf.loc[row, "name"]
                if "fluid_type" in column_names:
                    curr_obj_dict["fluid_type"] = gdf.loc[row, "fluid_type"]
                if "fluid_feature" in column_names:
                    curr_obj_dict["fluid_feature"] = gdf.loc[row, "fluid_feature"]
                if "fluid_feat" in column_names:
                    curr_obj_dict["fluid_feature"] = gdf.loc[row, "fluid_feat"]
                if "scenario" in column_names:
                    curr_obj_dict["scenario"] = gdf.loc[row, "scenario"]
                curr_obj_dict["topological_type"] = "PolyLine"
                curr_obj_dict["vtk_obj"] = PolyLine()
                
                if gdf.geom_type[row] == "LineString":
                    outXYZ = np_array(gdf.loc[row].geometry)

                    if np_shape(outXYZ)[1] == 2:
                        outZ = np_zeros((np_shape(outXYZ)[0], 1))
                        # print("outZ:\n", outZ)
                        outXYZ = np_column_stack((outXYZ, outZ))
                    # print("outXYZ:\n", outXYZ)
                    curr_obj_dict["vtk_obj"].points = outXYZ
                    curr_obj_dict["vtk_obj"].auto_cells()
                
                elif gdf.geom_type[row] == "MultiLineString":
                    outXYZ_list = np_array(gdf.loc[row].geometry)
                    vtkappend = vtkAppendPolyData()
                    for outXYZ in outXYZ_list:
                        temp_vtk = PolyLine()
                        if np_shape(outXYZ)[1] == 2:
                            outZ = np_zeros((np_shape(outXYZ)[0], 1))
                            # print("outZ:\n", outZ)
                            outXYZ = np_column_stack((outXYZ, outZ))
                        # print("outXYZ:\n", outXYZ)
                        temp_vtk.points = outXYZ
                        temp_vtk.auto_cells()
                        vtkappend.AddInputData(temp_vtk)
                    vtkappend.Update()
                    curr_obj_dict["vtk_obj"].ShallowCopy(vtkappend.GetOutput())
                """Create entity from the dictionary and run left_right."""
                if curr_obj_dict["vtk_obj"].points_number > 0:
                    output_uid = self.fluids_coll.add_entity_from_dict(curr_obj_dict)
                else:
                    print("Empty object")
                # else:
                # except:
                #     print("Invalid object")
                del curr_obj_dict
        elif gdf.geom_type[0] == "Point":
            if "fluid_feat" in column_names:
                gdf_index = gdf.set_index("fluid_feat")
                feat_list = set(gdf_index.index)



                for i in feat_list:
                    curr_obj_dict = deepcopy(FluidsCollection.fluid_entity_dict)
                    if 'dip' in gdf.columns:
                        vtk_obj = Attitude()
                    else:
                        vtk_obj = VertexSet()

                    if "name" in column_names:
                        curr_obj_dict["name"] = pd_series(gdf_index.loc[i, "name"])[0]
                    if "fluid_type" in column_names:
                        curr_obj_dict["fluid_type"] = pd_series(gdf_index.loc[i, "fluid_type"])[0]
                    if "fluid_type" in column_names:
                        curr_obj_dict["fluid_type"] = pd_series(gdf_index.loc[i, "fluid_type"])[0]
                    if "fluid_feature" in column_names:
                        curr_obj_dict["fluid_feature"] = i
                    if "fluid_feat" in column_names:
                        curr_obj_dict["fluid_feature"] = i
                    if "scenario" in column_names:
                        curr_obj_dict["scenario"] = pd_series(gdf_index.loc[i, "scenario"])[0]

                    curr_obj_dict["topological_type"] = "VertexSet"
                    curr_obj_dict["vtk_obj"] = vtk_obj

                    gdf_index['coords'] = gdf_index.geometry.apply(lambda x: np_array(x)) # [Gabriele] add a coordinate column in the gdf_index dataframe
                    outXYZ = np_array([p for p in gdf_index.loc[i, 'coords']])

                    if outXYZ.ndim == 1:
                        outXYZ = outXYZ.reshape(-1,np_shape(outXYZ)[0])

                    if np_shape(outXYZ)[1] == 2:
                        outZ = np_zeros((np_shape(outXYZ)[0], 1))
                        # print("outZ:\n", outZ)
                        outXYZ = np_column_stack((outXYZ, outZ))


                    # print(np_shape(outXYZ))
                    curr_obj_dict["vtk_obj"].points = outXYZ


                    if curr_obj_dict["vtk_obj"].points_number > 1:
                        curr_obj_dict["vtk_obj"].auto_cells()
                        # print(curr_obj_dict["vtk_obj"].point_data_keys)
                        properties_names = curr_obj_dict["vtk_obj"].point_data_keys
                        properties_components = [curr_obj_dict["vtk_obj"].get_point_data_shape(key)[1] for key in properties_names]
                        curr_obj_dict['properties_names'] = properties_names
                        curr_obj_dict['properties_components'] = properties_components
                        self.fluids_coll.add_entity_from_dict(curr_obj_dict)
                        del curr_obj_dict
                    elif curr_obj_dict["vtk_obj"].points_number > 0:
                        curr_obj_dict["vtk_obj"].auto_cells()
                        # print(curr_obj_dict["vtk_obj"].point_data_keys)
                        properties_names = curr_obj_dict["vtk_obj"].point_data_keys
                        properties_components = [curr_obj_dict["vtk_obj"].get_point_data_shape(key)[1] for key in properties_names]
                        curr_obj_dict['properties_names'] = properties_names
                        curr_obj_dict['properties_components'] = properties_components
                        self.fluids_coll.add_entity_from_dict(curr_obj_dict)
                        del curr_obj_dict
            else:
                print('Incomplete data. At least the fluid_feature property must be present')
        else:
            print("Only Point and Line geometries can be imported - aborting.")
            return  # except:  #     self.TextTerminal.appendPlainText("SHP file not recognized ERROR.")
    elif collection == 'Fritto misto':
        if (gdf.geom_type[0] == "LineString") or (gdf.geom_type[0] == "MultiLineString"):
            for row in range(gdf.shape[0]):
                # print("____ROW: ", row)
                # print("geometry type: ", gdf.geom_type[row])
                curr_obj_dict = deepcopy(FrittoMistoCollection.fritto_entity_dict)
                # if gdf.is_valid[row] and not gdf.is_empty[row]:
                # try:
                if "name" in column_names:
                    curr_obj_dict["name"] = gdf.loc[row, "name"]
                if "frit_type" in column_names:
                    curr_obj_dict["fritto_type"] = gdf.loc[row, "frit_type"]
                if "fritto_feature" in column_names:
                    curr_obj_dict["fritto_feature"] = gdf.loc[row, "fritto_feature"]
                if "frit_feat" in column_names:
                    curr_obj_dict["fritto_feature"] = gdf.loc[row, "frit_feat"]
                
                curr_obj_dict["topological_type"] = "PolyLine"
                curr_obj_dict["vtk_obj"] = Fritti()
                
                if gdf.geom_type[row] == "LineString":
                    outXYZ = np_array(gdf.loc[row].geometry)
                    # print("outXYZ:\n", outXYZ)
                    if np_shape(outXYZ)[1] == 2:
                        outZ = np_zeros((np_shape(outXYZ)[0], 1))
                        # print("outZ:\n", outZ)
                        outXYZ = np_column_stack((outXYZ, outZ))
                    # print("outXYZ:\n", outXYZ)
                    if 'label' in column_names:
                        curr_obj_dict["vtk_obj"].create_fritto(name='name',annotation=gdf['label'].values,xyz=outXYZ,ann_type='line')
                    else:
                        curr_obj_dict["vtk_obj"].create_fritto(name='name',xyz=outXYZ,ann_type='line')
               
                elif gdf.geom_type[row] == "MultiLineString":
                    outXYZ_list = np_array(gdf.loc[row].geometry)
                    vtkappend = vtkAppendPolyData()
                    for outXYZ in outXYZ_list:
                        temp_vtk = PolyLine()
                        # print("outXYZ:\n", outXYZ)
                        # print("np_shape(outXYZ):\n", np_shape(outXYZ))
                        if np_shape(outXYZ)[1] == 2:
                            outZ = np_zeros((np_shape(outXYZ)[0], 1))
                            # print("outZ:\n", outZ)
                            outXYZ = np_column_stack((outXYZ, outZ))
                        # print("outXYZ:\n", outXYZ)
                        temp_vtk.points = outXYZ
                        temp_vtk.auto_cells()
                        
                        vtkappend.AddInputData(temp_vtk)
                    vtkappend.Update()

                    if 'label' in column_names:
                        out_vtk = PolyLine()
                        out_vtk.ShallowCopy(vtkappend.GetOutput())
                        out_vtk.set_field_data(name='name',data=gdf['label'].values)
                        curr_obj_dict["vtk_obj"].ShallowCopy(out_vtk)
                    else:
                        curr_obj_dict["vtk_obj"].ShallowCopy(vtkappend.GetOutput())
                """Create entity from the dictionary and run left_right."""
                


                if curr_obj_dict["vtk_obj"].points_number > 0:
                    self.fritti_coll.add_entity_from_dict(curr_obj_dict)
                else:
                    print("Empty object")
                # else:
                # except:
                #     print("Invalid object")
                del curr_obj_dict
        elif gdf.geom_type[0] == "Point":
            if "frit_feat" in column_names:
                gdf_index = gdf.set_index("frit_feat")
                feat_list = set(gdf_index.index)



                for i in feat_list:
                    curr_obj_dict = deepcopy(FrittoMistoCollection.fritto_entity_dict)
                    
                    vtk_obj = Fritti()

                    if "name" in column_names:
                        curr_obj_dict["name"] = pd_series(gdf_index.loc[i, "name"])[0]
                    if "frit_type" in column_names:
                        curr_obj_dict["fritto_type"] = pd_series(gdf_index.loc[i, "frit_type"])[0]
                    if "fritto_feature" in column_names:
                        curr_obj_dict["fritto_feature"] = i
                    if "frit_feat" in column_names:
                        curr_obj_dict["fritto_feature"] = i
                    


                    curr_obj_dict["topological_type"] = "VertexSet"
                    curr_obj_dict["vtk_obj"] = vtk_obj

                    gdf_index['coords'] = gdf_index.geometry.apply(lambda x: np_array(x)) # [Gabriele] add a coordinate column in the gdf_index dataframe
                    outXYZ = np_array([p for p in gdf_index.loc[i, 'coords']])

                    if outXYZ.ndim == 1:
                        outXYZ = outXYZ.reshape(-1,np_shape(outXYZ)[0])

                    if np_shape(outXYZ)[1] == 2:
                        outZ = np_zeros((np_shape(outXYZ)[0], 1))
                        # print("outZ:\n", outZ)
                        outXYZ = np_column_stack((outXYZ, outZ))
                    
                    if "label" in column_names:
                        curr_obj_dict["vtk_obj"].create_fritto(name='name',xyz=outXYZ,annotation=gdf['label'].values)
                    else:
                        curr_obj_dict["vtk_obj"].create_fritto(name='name',xyz=outXYZ)

                    if curr_obj_dict["vtk_obj"].points_number > 1:
                        # curr_obj_dict["vtk_obj"].auto_cells()
                        # print(curr_obj_dict["vtk_obj"].point_data_keys)
                        properties_names = curr_obj_dict["vtk_obj"].point_data_keys
                        properties_components = [curr_obj_dict["vtk_obj"].get_point_data_shape(key)[1] for key in properties_names]
                        curr_obj_dict['properties_names'] = properties_names
                        curr_obj_dict['properties_components'] = properties_components
                        
                        
                        self.fritti_coll.add_entity_from_dict(curr_obj_dict)
                        del curr_obj_dict
                    elif curr_obj_dict["vtk_obj"].points_number > 0:
                        # curr_obj_dict["vtk_obj"].auto_cells()
                        # print(curr_obj_dict["vtk_obj"].point_data_keys)
                        properties_names = curr_obj_dict["vtk_obj"].point_data_keys
                        properties_components = [curr_obj_dict["vtk_obj"].get_point_data_shape(key)[1] for key in properties_names]
                        curr_obj_dict['properties_names'] = properties_names
                        curr_obj_dict['properties_components'] = properties_components
                        self.fritti_coll.add_entity_from_dict(curr_obj_dict)
                        del curr_obj_dict
            else:
                print('Incomplete data. At least the frit_feature property must be present')
        else:
            print("Only Point and Line geometries can be imported - aborting.")
            return  # except:  #     self.TextTerminal.appendPlainText("SHP file not recognized ERROR.")