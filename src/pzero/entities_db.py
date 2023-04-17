from PyQt5.QtCore import QObject, pyqtSignal, QSortFilterProxyModel

from pzero.collections.background import BackgroundCollection
from pzero.collections.boundary import BoundaryCollection
from pzero.collections.dom import DomCollection
from pzero.collections.fluid import FluidsCollection
from pzero.collections.geological import GeologicalCollection
from pzero.collections.image import ImageCollection
from pzero.collections.mesh3d import Mesh3DCollection
from pzero.collections.well import WellCollection
from pzero.collections.xsection import XSectionCollection

import logging as log

collections_to_instantiate = dict(
    geol=GeologicalCollection,
    xsect=XSectionCollection,
    dom=DomCollection,
    image=ImageCollection,
    mesh3d=Mesh3DCollection,
    boundary=BoundaryCollection,
    well=WellCollection,
    fluids=FluidsCollection,
    backgrounds=BackgroundCollection)


class EntitiesDB(QObject):
    """
    Entities are grouped into collections
    """
    clearing_entities_db_signal = pyqtSignal(name="ClearingEntitiesDB")

    def __init__(self, parent=None):
        log.debug("Instantiating EntitiesDB")
        super().__init__(parent=parent)

        self.collections = {}
        self.collections_to_proxy = {}

    def clear(self):
        self.clearing_entities_db_signal.emit()

        self.collections.clear()
        self.collections_to_proxy.clear()

        for name, cls in collections_to_instantiate.items():
            self.instantiate_collection(name, cls)

    def get_collection_by_name(self, name):
        return self.collections[name]

    def get_proxy_by_name(self, name):
        return self.collections_to_proxy[name]

    def has_collection(self, name):
        return name in list(self.collections.keys())

    def instantiate_collection(self, name, cls_to_instantiate):
        self.collections[name] = cls_to_instantiate(parent=self)
        self.collections_to_proxy[name] = QSortFilterProxyModel(self)
        self.collections_to_proxy[name].setSourceModel(self.collections[name])

    def get_collections_with_properties(self):
        return [c for c in self.collections.values() if "properties_names" in c._df.columns]

    def get_collection_with_uid(self, uid):
        for collection in self.collections.values():
            if collection.has_uid(uid):
                return collection
        return None

    def remove_uid(self, uid):
        print(  f"Removing uid {uid} from all collections" )
        collection = self.get_collection_with_uid(uid)
        if collection is not None:
            collection.remove_entity(uid)
        else:
            log.warning(f"Could not find collection with uid {uid}")

