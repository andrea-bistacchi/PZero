"""legend_manager.py
PZero© Andrea Bistacchi"""

from PyQt5.QtWidgets import (
    QTreeWidgetItem,
    QColorDialog,
    QPushButton,
    QSpinBox,
    QDoubleSpinBox,
    QComboBox,
)
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QObject

from pandas import unique as pd_unique
from math import isnan


class Legend(QObject):
    """Legend for geological and all other entities.
    Dictionaries used to define types of legend columns."""

    geol_legend_dict = {
        "geological_type": "undef",
        "geological_feature": "undef",
        "geological_age": "undef",
        "geological_time": 0.0,
        "geological_sequence": "strati_0",
        "scenario": "undef",
        "color_R": int(255),
        "color_G": int(255),
        "color_B": int(255),
        "line_thick": 2.0,
        "point_size": 10.0,
        "opacity": int(100),
    }

    well_legend_dict = {
        "Loc ID": "undef",
        "geological_feature": "undef",
        "color_R": int(255),
        "color_G": int(255),
        "color_B": int(255),
        "line_thick": 2.0,
        "opacity": 100,
    }
    fluids_legend_dict = {
        "fluid_type": "undef",
        "fluid_feature": "undef",
        "fluid_age": "undef",
        "fluid_time": 0.0,
        # 'geological_sequence': "strati_0",
        "scenario": "undef",
        "color_R": int(255),
        "color_G": int(255),
        "color_B": int(255),
        "line_thick": 2.0,
        "point_size": 10.0,
        "opacity": 100,
    }
    backgrounds_legend_dict = {
        "background_type": "undef",
        "background_feature": "undef",
        # 'geological_sequence': "strati_0",
        "color_R": int(255),
        "color_G": int(255),
        "color_B": int(255),
        "line_thick": 2.0,
        "point_size": 10.0,
        "opacity": 100,
    }

    legend_type_dict = {
        "geological_type": str,
        "geological_feature": str,
        "geological_age": str,
        "geological_time": float,
        "geological_sequence": str,
        "fluid_type": str,
        "fluid_feature": str,
        "fluid_age": str,
        "fluid_time": float,
        "background_type": str,
        "background_feature": str,
        "scenario": str,
        "color_R": int,
        "color_G": int,
        "color_B": int,
        "line_thick": float,
        "point_size": float,
        "opacity": int,
    }

    others_legend_dict = {
        "other_type": ["XSection", "Boundary", "Mesh3D", "DOM", "Image"],
        "color_R": [255, 255, 255, 255, 255],
        "color_G": [255, 255, 255, 255, 255],
        "color_B": [255, 255, 255, 255, 255],
        "line_thick": [2.0, 2.0, 2.0, 1.0, 2.0],
        "point_size": [2.0, 2.0, 2.0, 1.0, 2.0],
        "opacity": [100, 100, 100, 100, 100],
    }

    def __init__(self, parent=None, *args, **kwargs):
        QObject.__init__(self, parent)

    def update_widget(self, parent=None):
        """Update the legend widget based on the legend table.
        The pattern to extract a cell value from a Pandas dataframe is: dataframe.loc[boolean_index_rows, boolean_index_columns].values[cell_id]
        The boolean indexes used by loc can be:
        - the name of a column (e.g. "color")
        - a boolean indexing series (i.e. a sequence of True and False values) obtained by one or more conditions applied on the dataframe
        - a numeric index or a range of indexes as used by iloc (i.e. 3 or 3:5)
        The method values[] applied at the end returns the cell value(s) at specified cell(s), otherwise a dataframe would be returned
        The function pd_unique() used above returns a list of unique values from a set of cells.
        TO ADD MORE PROPERTIES TO THE LEGEND, SIMPLY ADD MORE COLUMNS TO THE legend AND NEW WIDGETS HERE POINTING TO THE NEW COLUMNS
        Note that at and iat can be used to access a single value in a cell directly (so values[] is not required), but do not work with conditional indexing.
        """
        parent.LegendTreeWidget.clear()
        parent.LegendTreeWidget.setColumnCount(10)
        parent.LegendTreeWidget.setHeaderLabels(
            [
                "Type > Feature > Scenario",
                "R",
                "G",
                "B",
                "Color",
                "Line thickness",
                "Point size",
                "Opacity",
                "Geological Time",
                "Stratigraphic sequence",
                "Show edges",
                "Show nodes",
            ]
        )
        parent.LegendTreeWidget.setItemsExpandable(True)
        for other_type in pd_unique(parent.others_legend_df["other_type"]):
            color_R = parent.others_legend_df.loc[
                parent.others_legend_df["other_type"] == other_type, "color_R"
            ].values[0]
            color_G = parent.others_legend_df.loc[
                parent.others_legend_df["other_type"] == other_type, "color_G"
            ].values[0]
            color_B = parent.others_legend_df.loc[
                parent.others_legend_df["other_type"] == other_type, "color_B"
            ].values[0]
            line_thick = parent.others_legend_df.loc[
                parent.others_legend_df["other_type"] == other_type, "line_thick"
            ].values[0]
            point_size = parent.others_legend_df.loc[
                parent.others_legend_df["other_type"] == other_type, "point_size"
            ].values[0]
            opacity = parent.others_legend_df.loc[
                parent.others_legend_df["other_type"] == other_type, "opacity"
            ].values[0]

            "other_color_dialog_btn > QPushButton used to select color"
            other_color_dialog_btn = QPushButton()
            other_color_dialog_btn.other_type = (
                other_type  # this is to pass these values to the update function below
            )
            other_color_dialog_btn.setStyleSheet(
                "background-color:rgb({},{},{})".format(color_R, color_G, color_B)
            )
            "other_line_thick_spn > QSpinBox used to select line thickness"
            other_line_thick_spn = QSpinBox()
            other_line_thick_spn.other_type = (
                other_type  # this is to pass these values to the update function below
            )
            other_line_thick_spn.setValue(line_thick)
            "other_point_size_spn > QSpinBox used to select point size"
            other_point_size_spn = QSpinBox()
            other_point_size_spn.other_type = (
                other_type  # this is to pass these values to the update function below
            )
            other_point_size_spn.setValue(point_size)
            "other_opacity_spn > QSpinBox used to select opacity"
            other_opacity_spn = QSpinBox()
            other_opacity_spn.setMaximum(100)
            other_opacity_spn.other_type = (
                other_type  # this is to pass these values to the update function below
            )
            other_opacity_spn.setValue(opacity)
            "IN THE FUTURE add QComboBox() here to show/hide mesh edges___________"
            "IN THE FUTURE add QComboBox() here to show/hide points___________"
            "Create items"
            llevel_1 = QTreeWidgetItem(
                parent.LegendTreeWidget,
                [other_type, str(color_R), str(color_G), str(color_B)],
            )  # self.GeologyTreeWidget as parent -> top level
            parent.LegendTreeWidget.setItemWidget(llevel_1, 4, other_color_dialog_btn)
            parent.LegendTreeWidget.setItemWidget(llevel_1, 5, other_line_thick_spn)
            if other_type == "DOM":
                parent.LegendTreeWidget.setItemWidget(llevel_1, 6, other_point_size_spn)
                other_point_size_spn.valueChanged.connect(
                    lambda: self.change_other_feature_point_size(parent=parent)
                )
            parent.LegendTreeWidget.setItemWidget(llevel_1, 7, other_opacity_spn)

            "Set signals for the widgets below"
            other_color_dialog_btn.clicked.connect(
                lambda: self.change_other_feature_color(parent=parent)
            )
            other_line_thick_spn.valueChanged.connect(
                lambda: self.change_other_feature_line_thick(parent=parent)
            )
            other_opacity_spn.valueChanged.connect(
                lambda: self.change_other_feature_opacity(parent=parent)
            )

        for geo_type in pd_unique(parent.geol_legend_df["geological_type"]):
            llevel_1 = QTreeWidgetItem(
                parent.LegendTreeWidget, [geo_type]
            )  # self.GeologyTreeWidget as parent -> top level
            for feature in pd_unique(
                parent.geol_legend_df.loc[
                    parent.geol_legend_df["geological_type"] == geo_type,
                    "geological_feature",
                ]
            ):
                llevel_2 = QTreeWidgetItem(
                    llevel_1, [feature]
                )  # llevel_1 as parent -> 2nd level
                for scenario in pd_unique(
                    parent.geol_legend_df.loc[
                        (parent.geol_legend_df["geological_type"] == geo_type)
                        & (parent.geol_legend_df["geological_feature"] == feature),
                        "scenario",
                    ]
                ):
                    color_R = parent.geol_legend_df.loc[
                        (parent.geol_legend_df["geological_type"] == geo_type)
                        & (parent.geol_legend_df["geological_feature"] == feature)
                        & (parent.geol_legend_df["scenario"] == scenario),
                        "color_R",
                    ].values[0]
                    color_G = parent.geol_legend_df.loc[
                        (parent.geol_legend_df["geological_type"] == geo_type)
                        & (parent.geol_legend_df["geological_feature"] == feature)
                        & (parent.geol_legend_df["scenario"] == scenario),
                        "color_G",
                    ].values[0]
                    color_B = parent.geol_legend_df.loc[
                        (parent.geol_legend_df["geological_type"] == geo_type)
                        & (parent.geol_legend_df["geological_feature"] == feature)
                        & (parent.geol_legend_df["scenario"] == scenario),
                        "color_B",
                    ].values[0]
                    line_thick = parent.geol_legend_df.loc[
                        (parent.geol_legend_df["geological_type"] == geo_type)
                        & (parent.geol_legend_df["geological_feature"] == feature)
                        & (parent.geol_legend_df["scenario"] == scenario),
                        "line_thick",
                    ].values[0]
                    point_size = parent.geol_legend_df.loc[
                        (parent.geol_legend_df["geological_type"] == geo_type)
                        & (parent.geol_legend_df["geological_feature"] == feature)
                        & (parent.geol_legend_df["scenario"] == scenario),
                        "point_size",
                    ].values[0]
                    opacity = parent.geol_legend_df.loc[
                        (parent.geol_legend_df["geological_type"] == geo_type)
                        & (parent.geol_legend_df["geological_feature"] == feature)
                        & (parent.geol_legend_df["scenario"] == scenario),
                        "opacity",
                    ].values[0]
                    geol_time_value = parent.geol_legend_df.loc[
                        (parent.geol_legend_df["geological_type"] == geo_type)
                        & (parent.geol_legend_df["geological_feature"] == feature)
                        & (parent.geol_legend_df["scenario"] == scenario),
                        "geological_time",
                    ].values[0]
                    # geol_time_value = str(parent.geol_legend_df.loc[(parent.geol_legend_df['geological_type'] == geo_type) & (parent.geol_legend_df['geological_feature'] == feature) & (parent.geol_legend_df['scenario'] == scenario), "geological_time"].values[0])
                    # if np.isnan(geol_time_value):
                    #     print("geol_time_value: ", geol_time_value)
                    #     geol_time_value = 0.0
                    #     print("geol_time_value: ", geol_time_value)
                    geol_sequence_value = parent.geol_legend_df.loc[
                        (parent.geol_legend_df["geological_type"] == geo_type)
                        & (parent.geol_legend_df["geological_feature"] == feature)
                        & (parent.geol_legend_df["scenario"] == scenario),
                        "geological_sequence",
                    ].values[0]
                    # if not isinstance(geol_sequence_value, str):
                    #     print("geol_sequence_value: ", geol_sequence_value)
                    #     geol_sequence_value = "strati_0"
                    #     print("geol_sequence_value: ", geol_sequence_value)
                    "geol_color_dialog_btn > QPushButton used to select color"
                    geol_color_dialog_btn = QPushButton()
                    geol_color_dialog_btn.geo_type = geo_type  # this is to pass these values to the update function below
                    geol_color_dialog_btn.feature = feature
                    geol_color_dialog_btn.scenario = scenario
                    geol_color_dialog_btn.setStyleSheet(
                        "background-color:rgb({},{},{})".format(
                            color_R, color_G, color_B
                        )
                    )
                    "geol_line_thick_spn > QSpinBox used to select line thickness"
                    geol_line_thick_spn = QSpinBox()
                    geol_line_thick_spn.geo_type = geo_type  # this is to pass these values to the update function below
                    geol_line_thick_spn.feature = feature
                    geol_line_thick_spn.scenario = scenario
                    geol_line_thick_spn.setValue(line_thick)
                    "geol_point_size_spn > QSpinBox used to select point size"
                    geol_point_size_spn = QSpinBox()
                    geol_point_size_spn.geo_type = geo_type  # this is to pass these values to the update function below
                    geol_point_size_spn.feature = feature
                    geol_point_size_spn.scenario = scenario
                    if isnan(point_size):
                        point_size = 0
                    geol_point_size_spn.setValue(point_size)
                    "geol_line_opacity_spn > QSpinBox used to select opacity"
                    geol_opacity_spn = QSpinBox()
                    geol_opacity_spn.geo_type = geo_type  # this is to pass these values to the update function below
                    geol_opacity_spn.feature = feature
                    geol_opacity_spn.scenario = scenario
                    geol_opacity_spn.setMaximum(100)
                    if isnan(opacity):
                        opacity = 0
                    geol_opacity_spn.setValue(opacity)
                    "geol_time_spn > QDoubleSpinBox used to give relative geological time"
                    geol_time_spn = QDoubleSpinBox()
                    geol_time_spn.setMinimum(-999999.0)  # no negative relative ages
                    geol_time_spn.geo_type = geo_type  # this is to pass these values to the update function below
                    geol_time_spn.feature = feature
                    geol_time_spn.scenario = scenario
                    geol_time_spn.setValue(geol_time_value)
                    # "geol_time_combo > QComboBox used to define relative geological time"
                    # geol_time_combo = QComboBox()
                    # geol_time_combo.setEditable(True)
                    # geol_time_combo.geo_type = geo_type  # this is to pass these values to the update function below
                    # geol_time_combo.feature = feature
                    # geol_time_combo.scenario = scenario
                    # geol_time_combo.addItems(parent.geol_legend_df['geological_time'].unique().astype(str))
                    # geol_time_combo.setCurrentText(geol_time_value)
                    "geol_sequence_combo > QComboBox used to define geological sequence"
                    geol_sequence_combo = QComboBox()
                    geol_sequence_combo.setEditable(True)
                    geol_sequence_combo.geo_type = geo_type  # this is to pass these values to the update function below
                    geol_sequence_combo.feature = feature
                    geol_sequence_combo.scenario = scenario
                    geol_sequence_combo.addItems(
                        parent.geol_legend_df["geological_sequence"].unique()
                    )
                    geol_sequence_combo.setCurrentText(geol_sequence_value)
                    "IN THE FUTURE add QComboBox() to show/hide mesh edges___________"
                    "IN THE FUTURE add QComboBox() to show/hide points___________"
                    "Create items"
                    llevel_3 = QTreeWidgetItem(
                        llevel_2, [scenario, str(color_R), str(color_G), str(color_B)]
                    )  # llevel_2 as parent -> 3rd level
                    parent.LegendTreeWidget.setItemWidget(
                        llevel_3, 4, geol_color_dialog_btn
                    )
                    parent.LegendTreeWidget.setItemWidget(
                        llevel_3, 5, geol_line_thick_spn
                    )
                    parent.LegendTreeWidget.setItemWidget(
                        llevel_3, 6, geol_point_size_spn
                    )
                    parent.LegendTreeWidget.setItemWidget(llevel_3, 7, geol_opacity_spn)
                    parent.LegendTreeWidget.setItemWidget(llevel_3, 8, geol_time_spn)
                    # parent.LegendTreeWidget.setItemWidget(llevel_3, 6, geol_time_combo)
                    parent.LegendTreeWidget.setItemWidget(
                        llevel_3, 9, geol_sequence_combo
                    )
                    "Set signals for the widgets below"
                    geol_color_dialog_btn.clicked.connect(
                        lambda: self.change_geology_feature_color(parent=parent)
                    )
                    geol_line_thick_spn.valueChanged.connect(
                        lambda: self.change_geology_feature_line_thick(parent=parent)
                    )
                    geol_point_size_spn.valueChanged.connect(
                        lambda: self.change_geology_feature_point_size(parent=parent)
                    )
                    geol_opacity_spn.valueChanged.connect(
                        lambda: self.change_geology_feature_opacity(parent=parent)
                    )
                    geol_time_spn.editingFinished.connect(
                        lambda: self.change_geological_time(parent=parent)
                    )
                    # geol_time_combo.currentTextChanged.connect(lambda: self.change_geological_time(parent=parent))
                    geol_sequence_combo.currentTextChanged.connect(
                        lambda: self.change_geological_sequence(parent=parent)
                    )
        for locid in pd_unique(parent.well_legend_df["Loc ID"]):
            llevel_1 = QTreeWidgetItem(
                parent.LegendTreeWidget, ["Wells"]
            )  # self.GeologyTreeWidget as parent -> top level

            llevel_2 = QTreeWidgetItem(
                llevel_1, [locid]
            )  # llevel_1 as parent -> 2nd level

            color_R = parent.well_legend_df.loc[
                parent.well_legend_df["Loc ID"] == locid, "color_R"
            ].values[0]

            color_G = parent.well_legend_df.loc[
                parent.well_legend_df["Loc ID"] == locid, "color_G"
            ].values[0]

            color_B = parent.well_legend_df.loc[
                parent.well_legend_df["Loc ID"] == locid, "color_B"
            ].values[0]

            line_thick = parent.well_legend_df.loc[
                parent.well_legend_df["Loc ID"] == locid, "line_thick"
            ].values[0]
            opacity = parent.well_legend_df.loc[
                parent.well_legend_df["Loc ID"] == locid, "opacity"
            ].values[0]
            # print(line_thick)

            # if not isinstance(geol_sequence_value, str):
            #     print("geol_sequence_value: ", geol_sequence_value)
            #     geol_sequence_value = "strati_0"
            #     print("geol_sequence_value: ", geol_sequence_value)
            "well_color_dialog_btn > QPushButton used to select color"
            well_color_dialog_btn = QPushButton()
            well_color_dialog_btn.locid = (
                locid  # this is to pass these values to the update function below
            )
            well_color_dialog_btn.setStyleSheet(
                "background-color:rgb({},{},{})".format(color_R, color_G, color_B)
            )
            "well_line_thick_spn > QSpinBox used to select line thickness"
            well_line_thick_spn = QSpinBox()
            well_line_thick_spn.locid = (
                locid  # this is to pass these values to the update function below
            )
            well_line_thick_spn.setValue(line_thick)
            "well_line_opacity_spn > QSpinBox used to select line thickness"
            well_line_opacity_spn = QSpinBox()
            well_line_opacity_spn.locid = locid
            well_line_opacity_spn.setMaximum(100)
            well_line_opacity_spn.setValue(opacity)

            "Create items"
            parent.LegendTreeWidget.setItemWidget(llevel_2, 4, well_color_dialog_btn)
            parent.LegendTreeWidget.setItemWidget(llevel_2, 5, well_line_thick_spn)
            parent.LegendTreeWidget.setItemWidget(llevel_2, 7, well_line_opacity_spn)

            "Set signals for the widgets below"
            well_color_dialog_btn.clicked.connect(
                lambda: self.change_well_color(parent=parent)
            )
            well_line_thick_spn.valueChanged.connect(
                lambda: self.change_well_line_thick(parent=parent)
            )
            well_line_opacity_spn.valueChanged.connect(
                lambda: self.change_well_line_opacity(parent=parent)
            )
        for fluid_type in pd_unique(parent.fluids_legend_df["fluid_type"]):
            llevel_1 = QTreeWidgetItem(
                parent.LegendTreeWidget, [fluid_type]
            )  # self.GeologyTreeWidget as parent -> top level
            for feature in pd_unique(
                parent.fluids_legend_df.loc[
                    parent.fluids_legend_df["fluid_type"] == fluid_type, "fluid_feature"
                ]
            ):
                llevel_2 = QTreeWidgetItem(
                    llevel_1, [feature]
                )  # llevel_1 as parent -> 2nd level
                for scenario in pd_unique(
                    parent.fluids_legend_df.loc[
                        (parent.fluids_legend_df["fluid_type"] == fluid_type)
                        & (parent.fluids_legend_df["fluid_feature"] == feature),
                        "scenario",
                    ]
                ):
                    color_R = parent.fluids_legend_df.loc[
                        (parent.fluids_legend_df["fluid_type"] == fluid_type)
                        & (parent.fluids_legend_df["fluid_feature"] == feature)
                        & (parent.fluids_legend_df["scenario"] == scenario),
                        "color_R",
                    ].values[0]
                    color_G = parent.fluids_legend_df.loc[
                        (parent.fluids_legend_df["fluid_type"] == fluid_type)
                        & (parent.fluids_legend_df["fluid_feature"] == feature)
                        & (parent.fluids_legend_df["scenario"] == scenario),
                        "color_G",
                    ].values[0]
                    color_B = parent.fluids_legend_df.loc[
                        (parent.fluids_legend_df["fluid_type"] == fluid_type)
                        & (parent.fluids_legend_df["fluid_feature"] == feature)
                        & (parent.fluids_legend_df["scenario"] == scenario),
                        "color_B",
                    ].values[0]
                    line_thick = parent.fluids_legend_df.loc[
                        (parent.fluids_legend_df["fluid_type"] == fluid_type)
                        & (parent.fluids_legend_df["fluid_feature"] == feature)
                        & (parent.fluids_legend_df["scenario"] == scenario),
                        "line_thick",
                    ].values[0]
                    point_size = parent.fluids_legend_df.loc[
                        (parent.fluids_legend_df["fluid_type"] == fluid_type)
                        & (parent.fluids_legend_df["fluid_feature"] == feature)
                        & (parent.fluids_legend_df["scenario"] == scenario),
                        "point_size",
                    ].values[0]
                    opacity = parent.fluids_legend_df.loc[
                        (parent.fluids_legend_df["fluid_type"] == fluid_type)
                        & (parent.fluids_legend_df["fluid_feature"] == feature)
                        & (parent.fluids_legend_df["scenario"] == scenario),
                        "opacity",
                    ].values[0]
                    fluid_time_value = parent.fluids_legend_df.loc[
                        (parent.fluids_legend_df["fluid_type"] == fluid_type)
                        & (parent.fluids_legend_df["fluid_feature"] == feature)
                        & (parent.fluids_legend_df["scenario"] == scenario),
                        "fluid_time",
                    ].values[0]

                    # geol_time_value = str(parent.geol_legend_df.loc[(parent.geol_legend_df['geological_type'] == geo_type) & (parent.geol_legend_df['geological_feature'] == feature) & (parent.geol_legend_df['scenario'] == scenario), "geological_time"].values[0])
                    # if np.isnan(geol_time_value):
                    #     print("geol_time_value: ", geol_time_value)
                    #     geol_time_value = 0.0
                    #     print("geol_time_value: ", geol_time_value)
                    # fluid_sequence_value = parent.fluids_legend_df.loc[(parent.fluids_legend_df['fluid_type'] == fluid_type) & (parent.fluids_legend_df['fluid_feature'] == feature) & (parent.fluids_legend_df['scenario'] == scenario), "fluid_sequence"].values[0]
                    # if not isinstance(geol_sequence_value, str):
                    #     print("geol_sequence_value: ", geol_sequence_value)
                    #     geol_sequence_value = "strati_0"
                    #     print("geol_sequence_value: ", geol_sequence_value)
                    "geol_color_dialog_btn > QPushButton used to select color"
                    fluid_color_dialog_btn = QPushButton()
                    fluid_color_dialog_btn.fluid_type = fluid_type  # this is to pass these values to the update function below
                    fluid_color_dialog_btn.feature = feature
                    fluid_color_dialog_btn.scenario = scenario
                    fluid_color_dialog_btn.setStyleSheet(
                        "background-color:rgb({},{},{})".format(
                            color_R, color_G, color_B
                        )
                    )
                    "fluid_line_thick_spn > QSpinBox used to select line thickness"
                    fluid_line_thick_spn = QSpinBox()
                    fluid_line_thick_spn.fluid_type = fluid_type  # this is to pass these values to the update function below
                    fluid_line_thick_spn.feature = feature
                    fluid_line_thick_spn.scenario = scenario
                    fluid_line_thick_spn.setValue(line_thick)
                    "fluid_point_size_spn > QSpinBox used to select point size"
                    fluid_point_size_spn = QSpinBox()
                    fluid_point_size_spn.fluid_type = fluid_type  # this is to pass these values to the update function below
                    fluid_point_size_spn.feature = feature
                    fluid_point_size_spn.scenario = scenario
                    fluid_point_size_spn.setValue(point_size)
                    "fluid_opacity_spn > QSpinBox used to select line thickness"
                    fluid_opacity_spn = QSpinBox()
                    fluid_opacity_spn.fluid_type = fluid_type  # this is to pass these values to the update function below
                    fluid_opacity_spn.feature = feature
                    fluid_opacity_spn.scenario = scenario
                    fluid_opacity_spn.setMaximum(100)
                    fluid_opacity_spn.setValue(opacity)
                    "geol_time_spn > QDoubleSpinBox used to give relative geological time"
                    fluid_time_spn = QDoubleSpinBox()
                    fluid_time_spn.setMinimum(-999999.0)  # no negative relative ages
                    fluid_time_spn.fluid_type = fluid_type  # this is to pass these values to the update function below
                    fluid_time_spn.feature = feature
                    fluid_time_spn.scenario = scenario
                    fluid_time_spn.setValue(fluid_time_value)
                    # "geol_time_combo > QComboBox used to define relative geological time"
                    # geol_time_combo = QComboBox()
                    # geol_time_combo.setEditable(True)
                    # geol_time_combo.geo_type = geo_type  # this is to pass these values to the update function below
                    # geol_time_combo.feature = feature
                    # geol_time_combo.scenario = scenario
                    # geol_time_combo.addItems(parent.geol_legend_df['geological_time'].unique().astype(str))
                    # geol_time_combo.setCurrentText(geol_time_value)
                    "geol_sequence_combo > QComboBox used to define geological sequence"
                    # geol_sequence_combo = QComboBox()
                    # geol_sequence_combo.setEditable(True)
                    # geol_sequence_combo.geo_type = geo_type  # this is to pass these values to the update function below
                    # geol_sequence_combo.feature = feature
                    # geol_sequence_combo.scenario = scenario
                    # geol_sequence_combo.addItems(parent.geol_legend_df['geological_sequence'].unique())
                    # geol_sequence_combo.setCurrentText(geol_sequence_value)
                    "IN THE FUTURE add QComboBox() to show/hide mesh edges___________"
                    "IN THE FUTURE add QComboBox() to show/hide points___________"
                    "Create items"
                    llevel_3 = QTreeWidgetItem(
                        llevel_2, [scenario, str(color_R), str(color_G), str(color_B)]
                    )  # llevel_2 as parent -> 3rd level
                    parent.LegendTreeWidget.setItemWidget(
                        llevel_3, 4, fluid_color_dialog_btn
                    )
                    parent.LegendTreeWidget.setItemWidget(
                        llevel_3, 5, fluid_line_thick_spn
                    )
                    parent.LegendTreeWidget.setItemWidget(
                        llevel_3, 6, fluid_point_size_spn
                    )
                    parent.LegendTreeWidget.setItemWidget(
                        llevel_3, 7, fluid_opacity_spn
                    )
                    parent.LegendTreeWidget.setItemWidget(llevel_3, 8, fluid_time_spn)
                    # parent.LegendTreeWidget.setItemWidget(llevel_3, 6, geol_time_combo)
                    # parent.LegendTreeWidget.setItemWidget(llevel_3, 7, geol_sequence_combo)
                    "Set signals for the widgets below"
                    fluid_color_dialog_btn.clicked.connect(
                        lambda: self.change_fluid_feature_color(parent=parent)
                    )
                    fluid_line_thick_spn.valueChanged.connect(
                        lambda: self.change_fluid_feature_line_thick(parent=parent)
                    )
                    fluid_point_size_spn.valueChanged.connect(
                        lambda: self.change_fluid_feature_point_size(parent=parent)
                    )
                    fluid_opacity_spn.valueChanged.connect(
                        lambda: self.change_fluid_feature_opacity(parent=parent)
                    )
                    fluid_time_spn.editingFinished.connect(
                        lambda: self.change_fluid_time(parent=parent)
                    )
                    # geol_time_combo.currentTextChanged.connect(lambda: self.change_geological_time(parent=parent))
                    # fluid_sequence_combo.currentTextChanged.connect(lambda: self.change_fluid_sequence(parent=parent))
        for background_type in pd_unique(
            parent.backgrounds_legend_df["background_type"]
        ):
            llevel_1 = QTreeWidgetItem(
                parent.LegendTreeWidget, [background_type]
            )  # self.GeologyTreeWidget as parent -> top level
            for feature in pd_unique(
                parent.backgrounds_legend_df.loc[
                    parent.backgrounds_legend_df["background_type"] == background_type,
                    "background_feature",
                ]
            ):
                llevel_2 = QTreeWidgetItem(
                    llevel_1, [feature]
                )  # llevel_1 as parent -> 2nd level
                color_R = parent.backgrounds_legend_df.loc[
                    (parent.backgrounds_legend_df["background_type"] == background_type)
                    & (parent.backgrounds_legend_df["background_feature"] == feature),
                    "color_R",
                ].values[0]
                color_G = parent.backgrounds_legend_df.loc[
                    (parent.backgrounds_legend_df["background_type"] == background_type)
                    & (parent.backgrounds_legend_df["background_feature"] == feature),
                    "color_G",
                ].values[0]
                color_B = parent.backgrounds_legend_df.loc[
                    (parent.backgrounds_legend_df["background_type"] == background_type)
                    & (parent.backgrounds_legend_df["background_feature"] == feature),
                    "color_B",
                ].values[0]
                line_thick = parent.backgrounds_legend_df.loc[
                    (parent.backgrounds_legend_df["background_type"] == background_type)
                    & (parent.backgrounds_legend_df["background_feature"] == feature),
                    "line_thick",
                ].values[0]
                point_size = parent.backgrounds_legend_df.loc[
                    (parent.backgrounds_legend_df["background_type"] == background_type)
                    & (parent.backgrounds_legend_df["background_feature"] == feature),
                    "point_size",
                ].values[0]
                opacity = parent.backgrounds_legend_df.loc[
                    (parent.backgrounds_legend_df["background_type"] == background_type)
                    & (parent.backgrounds_legend_df["background_feature"] == feature),
                    "opacity",
                ].values[0]
                "geol_color_dialog_btn > QPushButton used to select color"
                backgrounds_color_dialog_btn = QPushButton()
                backgrounds_color_dialog_btn.background_type = background_type  # this is to pass these values to the update function below
                backgrounds_color_dialog_btn.feature = feature

                backgrounds_color_dialog_btn.setStyleSheet(
                    "background-color:rgb({},{},{})".format(color_R, color_G, color_B)
                )
                "background_line_thick_spn > QSpinBox used to select line thickness"
                background_line_thick_spn = QSpinBox()
                background_line_thick_spn.background_type = background_type  # this is to pass these values to the update function below
                background_line_thick_spn.feature = feature

                background_line_thick_spn.setValue(line_thick)

                "background_point_size_spn > QSpinBox used to select line thickness"
                background_point_size_spn = QSpinBox()
                background_point_size_spn.background_type = background_type  # this is to pass these values to the update function below
                background_point_size_spn.feature = feature
                background_point_size_spn.setValue(point_size)
                "background_opacity_spn > QSpinBox used to select line thickness"
                background_opacity_spn = QSpinBox()
                background_opacity_spn.background_type = background_type  # this is to pass these values to the update function below
                background_opacity_spn.feature = feature
                background_opacity_spn.setMaximum(100)
                background_opacity_spn.setValue(opacity)

                "Create items"
                # llevel_3 = QTreeWidgetItem(llevel_2, [scenario, str(color_R), str(color_G), str(color_B)])  # llevel_2 as parent -> 3rd level
                parent.LegendTreeWidget.setItemWidget(
                    llevel_2, 4, backgrounds_color_dialog_btn
                )
                parent.LegendTreeWidget.setItemWidget(
                    llevel_2, 5, background_line_thick_spn
                )
                parent.LegendTreeWidget.setItemWidget(
                    llevel_2, 6, background_point_size_spn
                )
                parent.LegendTreeWidget.setItemWidget(
                    llevel_2, 7, background_opacity_spn
                )

                "Set signals for the widgets below"
                backgrounds_color_dialog_btn.clicked.connect(
                    lambda: self.change_background_feature_color(parent=parent)
                )
                background_line_thick_spn.valueChanged.connect(
                    lambda: self.change_background_feature_line_thick(parent=parent)
                )
                background_point_size_spn.valueChanged.connect(
                    lambda: self.change_background_feature_point_size(parent=parent)
                )
                background_opacity_spn.valueChanged.connect(
                    lambda: self.change_background_opacity(parent=parent)
                )

        parent.LegendTreeWidget.expandAll()

    def change_geology_feature_color(self, parent=None):
        geo_type = self.sender().geo_type
        feature = self.sender().feature
        scenario = self.sender().scenario
        """Here we use the same query as above to GET the color from the legend"""
        old_color_R = parent.geol_legend_df.loc[
            (parent.geol_legend_df["geological_type"] == geo_type)
            & (parent.geol_legend_df["geological_feature"] == feature)
            & (parent.geol_legend_df["scenario"] == scenario),
            "color_R",
        ].values[0]
        old_color_G = parent.geol_legend_df.loc[
            (parent.geol_legend_df["geological_type"] == geo_type)
            & (parent.geol_legend_df["geological_feature"] == feature)
            & (parent.geol_legend_df["scenario"] == scenario),
            "color_G",
        ].values[0]
        old_color_B = parent.geol_legend_df.loc[
            (parent.geol_legend_df["geological_type"] == geo_type)
            & (parent.geol_legend_df["geological_feature"] == feature)
            & (parent.geol_legend_df["scenario"] == scenario),
            "color_B",
        ].values[0]
        color_in = QColor(
            old_color_R, old_color_G, old_color_B
        )  # https://doc.qt.io/qtforpython/PySide2/QtGui/QColor.html#PySide2.QtGui.QColor
        color_out = QColorDialog.getColor(
            initial=color_in, title="Select color"
        )  # https://doc.qt.io/qtforpython/PySide2/QtWidgets/QColorDialog.html#PySide2.QtWidgets.PySide2.QtWidgets.QColorDialog.getColor
        if not color_out.isValid():
            color_out = color_in
        new_color_R = color_out.red()
        new_color_G = color_out.green()
        new_color_B = color_out.blue()
        """Here the query is reversed and modified, dropping the values() method, to allow SETTING the color in the legend."""
        parent.geol_legend_df.loc[
            (parent.geol_legend_df["geological_type"] == geo_type)
            & (parent.geol_legend_df["geological_feature"] == feature)
            & (parent.geol_legend_df["scenario"] == scenario),
            "color_R",
        ] = new_color_R
        parent.geol_legend_df.loc[
            (parent.geol_legend_df["geological_type"] == geo_type)
            & (parent.geol_legend_df["geological_feature"] == feature)
            & (parent.geol_legend_df["scenario"] == scenario),
            "color_G",
        ] = new_color_G
        parent.geol_legend_df.loc[
            (parent.geol_legend_df["geological_type"] == geo_type)
            & (parent.geol_legend_df["geological_feature"] == feature)
            & (parent.geol_legend_df["scenario"] == scenario),
            "color_B",
        ] = new_color_B
        """Update button color."""
        self.sender().setStyleSheet(
            "background-color:rgb({},{},{})".format(
                new_color_R, new_color_G, new_color_B
            )
        )
        """Signal to update actors in windows. This is emitted only for the modified uid under the 'color' key."""
        updated_list = parent.geol_coll.df.loc[
            (parent.geol_coll.df["geological_type"] == geo_type)
            & (parent.geol_coll.df["geological_feature"] == feature)
            & (parent.geol_coll.df["scenario"] == scenario),
            "uid",
        ].to_list()
        parent.geology_legend_color_modified_signal.emit(updated_list)
        # self.change_well_feature_color(parent,feature) #Update the wells

    def change_geology_feature_line_thick(self, parent=None):
        geo_type = self.sender().geo_type
        feature = self.sender().feature
        scenario = self.sender().scenario
        line_thick = self.sender().value()
        "Here the query is reversed and modified, dropping the values() method, to allow SETTING the line thickness in the legend"
        parent.geol_legend_df.loc[
            (parent.geol_legend_df["geological_type"] == geo_type)
            & (parent.geol_legend_df["geological_feature"] == feature)
            & (parent.geol_legend_df["scenario"] == scenario),
            "line_thick",
        ] = line_thick
        """Signal to update actors in windows. This is emitted only for the modified uid under the 'line_thick' key."""
        updated_list = parent.geol_coll.df.loc[
            (parent.geol_coll.df["geological_type"] == geo_type)
            & (parent.geol_coll.df["geological_feature"] == feature)
            & (parent.geol_coll.df["scenario"] == scenario),
            "uid",
        ].to_list()
        parent.geology_legend_thick_modified_signal.emit(updated_list)

    def change_geology_feature_point_size(self, parent=None):
        geo_type = self.sender().geo_type
        feature = self.sender().feature
        scenario = self.sender().scenario
        point_size = self.sender().value()
        "Here the query is reversed and modified, dropping the values() method, to allow SETTING the line thickness in the legend"
        parent.geol_legend_df.loc[
            (parent.geol_legend_df["geological_type"] == geo_type)
            & (parent.geol_legend_df["geological_feature"] == feature)
            & (parent.geol_legend_df["scenario"] == scenario),
            "point_size",
        ] = point_size
        """Signal to update actors in windows. This is emitted only for the modified uid under the 'line_thick' key."""
        updated_list = parent.geol_coll.df.loc[
            (parent.geol_coll.df["geological_type"] == geo_type)
            & (parent.geol_coll.df["geological_feature"] == feature)
            & (parent.geol_coll.df["scenario"] == scenario),
            "uid",
        ].to_list()
        parent.geology_legend_point_size_modified_signal.emit(updated_list)

    def change_geology_feature_opacity(self, parent=None):
        geo_type = self.sender().geo_type
        feature = self.sender().feature
        scenario = self.sender().scenario
        opacity = self.sender().value()
        "Here the query is reversed and modified, dropping the values() method, to allow SETTING the line thickness in the legend"
        parent.geol_legend_df.loc[
            (parent.geol_legend_df["geological_type"] == geo_type)
            & (parent.geol_legend_df["geological_feature"] == feature)
            & (parent.geol_legend_df["scenario"] == scenario),
            "opacity",
        ] = opacity
        """Signal to update actors in windows. This is emitted only for the modified uid under the 'opacity' key."""
        updated_list = parent.geol_coll.df.loc[
            (parent.geol_coll.df["geological_type"] == geo_type)
            & (parent.geol_coll.df["geological_feature"] == feature)
            & (parent.geol_coll.df["scenario"] == scenario),
            "uid",
        ].to_list()
        parent.geology_legend_opacity_modified_signal.emit(updated_list)

    def change_geological_time(self, parent=None):
        geo_type = self.sender().geo_type
        feature = self.sender().feature
        scenario = self.sender().scenario
        geol_time = self.sender().value()
        parent.geol_legend_df.loc[
            (parent.geol_legend_df["geological_type"] == geo_type)
            & (parent.geol_legend_df["geological_feature"] == feature)
            & (parent.geol_legend_df["scenario"] == scenario),
            "geological_time",
        ] = geol_time
        """Order geological legend entities with descending geological_time values"""
        parent.geol_legend_df.sort_values(
            by="geological_time", ascending=True, inplace=True
        )
        """THE FOLLOWING MUST BE CHANGED IN A SORT COMMAND
        UPDATE AT THE MOMENT DOES NOT WORK PROPERLY"""
        # parent.LegendTreeWidget.setSortingEnabled(True)
        # parent.LegendTreeWidget.sortByColumn(7, Qt.AscendingOrder)
        # parent.LegendTreeWidget.setSortingEnabled(False)
        # try:
        #     geol_time = float(self.sender().currentText())
        # except:
        #     geol_time = float('nan')
        #     parent.geol_legend_df.loc[(parent.geol_legend_df['geological_type'] == geo_type) & (parent.geol_legend_df['geological_feature'] == feature) & (parent.geol_legend_df['scenario'] == scenario), "geological_time"] = geol_time
        #     """Order geological legend entities with descending geological_time values"""
        #     parent.geol_legend_df.sort_values(by='geological_time', ascending=True, inplace=True)
        #     self.update_widget(parent=parent)

    def change_geological_sequence(self, parent=None):
        geo_type = self.sender().geo_type
        feature = self.sender().feature
        scenario = self.sender().scenario
        geol_seqn = self.sender().currentText()
        parent.geol_legend_df.loc[
            (parent.geol_legend_df["geological_type"] == geo_type)
            & (parent.geol_legend_df["geological_feature"] == feature)
            & (parent.geol_legend_df["scenario"] == scenario),
            "geological_sequence",
        ] = geol_seqn
        """THE FOLLOWING MUST BE CHANGED IN A FOR LOOP OVER ALL ITEMS IN COLUMN 7
        parent.LegendTreeWidget.setItemWidget(llevel_3, 7, geol_sequence_combo)
        UPDATING THE VALUES AS IN
        geol_sequence_combo.addItems(parent.geol_legend_df['geological_sequence'].unique())"""

    def change_other_feature_color(self, parent=None):
        other_type = self.sender().other_type
        """Here we use the same query as above to GET the color from the legend"""
        old_color_R = parent.others_legend_df.loc[
            (parent.others_legend_df["other_type"] == other_type), "color_R"
        ].values[0]
        old_color_G = parent.others_legend_df.loc[
            (parent.others_legend_df["other_type"] == other_type), "color_G"
        ].values[0]
        old_color_B = parent.others_legend_df.loc[
            (parent.others_legend_df["other_type"] == other_type), "color_B"
        ].values[0]
        color_in = QColor(
            old_color_R, old_color_G, old_color_B
        )  # https://doc.qt.io/qtforpython/PySide2/QtGui/QColor.html#PySide2.QtGui.QColor
        color_out = QColorDialog.getColor(
            initial=color_in, title="Select color"
        )  # https://doc.qt.io/qtforpython/PySide2/QtWidgets/QColorDialog.html#PySide2.QtWidgets.PySide2.QtWidgets.QColorDialog.getColor
        if not color_out.isValid():
            color_out = color_in
        new_color_R = color_out.red()
        new_color_G = color_out.green()
        new_color_B = color_out.blue()
        """Here the query is reversed and modified, dropping the values() method, to allow SETTING the color in the legend."""
        parent.others_legend_df.loc[
            (parent.others_legend_df["other_type"] == other_type), "color_R"
        ] = new_color_R
        parent.others_legend_df.loc[
            (parent.others_legend_df["other_type"] == other_type), "color_G"
        ] = new_color_G
        parent.others_legend_df.loc[
            (parent.others_legend_df["other_type"] == other_type), "color_B"
        ] = new_color_B
        """Update button color."""
        self.sender().setStyleSheet(
            "background-color:rgb({},{},{})".format(
                new_color_R, new_color_G, new_color_B
            )
        )
        """Signals to update actors in windows. This is emitted only for the modified uid under the 'color' key."""
        if other_type == "XSection":
            parent.xsect_legend_color_modified_signal.emit(
                parent.xsect_coll.df["uid"].tolist()
            )
        elif other_type == "DOM":
            parent.dom_legend_color_modified_signal.emit(
                parent.dom_coll.df["uid"].tolist()
            )
        elif other_type == "Mesh3D":
            parent.mesh3d_legend_color_modified_signal.emit(
                parent.dom_coll.df["uid"].tolist()
            )
        elif other_type == "Boundary":
            parent.boundary_legend_color_modified_signal.emit(
                parent.boundary_coll.df["uid"].tolist()
            )

    def change_other_feature_line_thick(self, parent=None):
        other_type = self.sender().other_type
        line_thick = self.sender().value()
        "Here the query is reversed and modified, dropping the values() method, to allow SETTING the line thickness in the legend"
        parent.others_legend_df.loc[
            (parent.others_legend_df["other_type"] == other_type), "line_thick"
        ] = line_thick
        """Signals to update actors in windows. This is emitted only for the modified uid under the 'color' key."""
        if other_type == "XSection":
            parent.xsect_legend_thick_modified_signal.emit(
                parent.xsect_coll.df["uid"].tolist()
            )
        elif other_type == "DOM":
            parent.dom_legend_thick_modified_signal.emit(
                parent.dom_coll.df["uid"].tolist()
            )
        elif other_type == "Mesh3D":
            parent.mesh3d_legend_thick_modified_signal.emit(
                parent.dom_coll.df["uid"].tolist()
            )
        elif other_type == "Boundary":
            parent.boundary_legend_thick_modified_signal.emit(
                parent.boundary_coll.df["uid"].tolist()
            )

    def change_other_feature_point_size(self, parent=None):
        other_type = self.sender().other_type
        point_size = self.sender().value()
        "Here the query is reversed and modified, dropping the values() method, to allow SETTING the line thickness in the legend"
        parent.others_legend_df.loc[
            (parent.others_legend_df["other_type"] == other_type), "point_size"
        ] = point_size
        """Signals to update actors in windows. This is emitted only for the modified uid under the 'color' key."""
        # if other_type == "XSection":
        #     parent.xsect_legend_point_size_modified_signal.emit(parent.xsect_coll.df['uid'].tolist())
        if other_type == "DOM":
            parent.dom_legend_point_size_modified_signal.emit(
                parent.dom_coll.df["uid"].tolist()
            )
        # elif other_type == "Mesh3D":
        #     parent.mesh3d_legend_point_size_modified_signal.emit(parent.dom_coll.df['uid'].tolist())
        # elif other_type == "Boundary":
        #     parent.boundary_legend_point_size_modified_signal.emit(parent.boundary_coll.df['uid'].tolist())

    def change_other_feature_opacity(self, parent=None):
        other_type = self.sender().other_type
        opacity = self.sender().value()
        "Here the query is reversed and modified, dropping the values() method, to allow SETTING the line thickness in the legend"
        parent.others_legend_df.loc[
            (parent.others_legend_df["other_type"] == other_type), "opacity"
        ] = opacity
        """Signals to update actors in windows. This is emitted only for the modified uid under the 'color' key."""
        if other_type == "XSection":
            parent.xsect_legend_opacity_modified_signal.emit(
                parent.xsect_coll.df["uid"].tolist()
            )
        elif other_type == "DOM":
            parent.dom_legend_opacity_modified_signal.emit(
                parent.dom_coll.df["uid"].tolist()
            )
        elif other_type == "Mesh3D":
            parent.mesh3d_legend_opacity_modified_signal.emit(
                parent.dom_coll.df["uid"].tolist()
            )
        elif other_type == "Boundary":
            parent.boundary_legend_opacity_modified_signal.emit(
                parent.boundary_coll.df["uid"].tolist()
            )
        elif other_type == "Image":
            parent.image_legend_opacity_modified_signal.emit(
                parent.image_coll.df["uid"].tolist()
            )

    def change_well_color(self, parent=None, feature=None):
        # well_id = parent.geol_coll_df.loc[parent.geol_coll_df['uid'] == uid]

        locid = self.sender().locid

        """Here we use the same query as above to GET the color from the legend"""
        old_color_R = parent.well_legend_df.loc[
            parent.well_legend_df["Loc ID"] == locid, "color_R"
        ].values[0]

        old_color_G = parent.well_legend_df.loc[
            parent.well_legend_df["Loc ID"] == locid, "color_G"
        ].values[0]

        old_color_B = parent.well_legend_df.loc[
            parent.well_legend_df["Loc ID"] == locid, "color_B"
        ].values[0]

        color_in = QColor(
            old_color_R, old_color_G, old_color_B
        )  # https://doc.qt.io/qtforpython/PySide2/QtGui/QColor.html#PySide2.QtGui.QColor
        color_out = QColorDialog.getColor(
            initial=color_in, title="Select color"
        )  # https://doc.qt.io/qtforpython/PySide2/QtWidgets/QColorDialog.html#PySide2.QtWidgets.PySide2.QtWidgets.QColorDialog.getColor
        if not color_out.isValid():
            color_out = color_in
        new_color_R = color_out.red()
        new_color_G = color_out.green()
        new_color_B = color_out.blue()

        """Here the query is reversed and modified, dropping the values() method, to allow SETTING the color in the legend."""

        parent.well_legend_df.loc[
            parent.well_legend_df["Loc ID"] == locid, "color_R"
        ] = new_color_R

        parent.well_legend_df.loc[
            parent.well_legend_df["Loc ID"] == locid, "color_G"
        ] = new_color_G

        parent.well_legend_df.loc[
            parent.well_legend_df["Loc ID"] == locid, "color_B"
        ] = new_color_B

        """Update button color."""
        self.sender().setStyleSheet(
            "background-color:rgb({},{},{})".format(
                new_color_R, new_color_G, new_color_B
            )
        )

        """Signal to update actors in windows. This is emitted only for the modified uid under the 'color' key."""
        updated_list = parent.well_coll.df.loc[
            parent.well_legend_df["Loc ID"] == locid, "uid"
        ].to_list()
        parent.well_legend_color_modified_signal.emit(updated_list)

    def change_well_line_thick(self, parent=None):
        locid = self.sender().locid
        line_thick = self.sender().value()
        "Here the query is reversed and modified, dropping the values() method, to allow SETTING the line thickness in the legend"
        parent.well_legend_df.loc[
            parent.well_legend_df["Loc ID"] == locid, "line_thick"
        ] = line_thick
        """Signal to update actors in windows. This is emitted only for the modified uid under the 'line_thick' key."""
        updated_list = parent.well_coll.df.loc[
            parent.well_coll.df["Loc ID"] == locid, "uid"
        ].to_list()
        # print(updated_list)
        parent.well_legend_thick_modified_signal.emit(updated_list)

    def change_well_line_opacity(self, parent=None):
        locid = self.sender().locid
        opacity = self.sender().value()
        "Here the query is reversed and modified, dropping the values() method, to allow SETTING the line thickness in the legend"
        parent.well_legend_df.loc[
            parent.well_legend_df["Loc ID"] == locid, "opacity"
        ] = opacity
        """Signal to update actors in windows. This is emitted only for the modified uid under the 'line_thick' key."""
        updated_list = parent.well_coll.df.loc[
            parent.well_coll.df["Loc ID"] == locid, "uid"
        ].to_list()
        # print(updated_list)
        parent.well_legend_opacity_modified_signal.emit(updated_list)

    def change_fluid_feature_color(self, parent=None):
        fluid_type = self.sender().fluid_type
        feature = self.sender().feature
        scenario = self.sender().scenario
        """Here we use the same query as above to GET the color from the legend"""
        old_color_R = parent.fluids_legend_df.loc[
            (parent.fluids_legend_df["fluid_type"] == fluid_type)
            & (parent.fluids_legend_df["fluid_feature"] == feature)
            & (parent.fluids_legend_df["scenario"] == scenario),
            "color_R",
        ].values[0]
        old_color_G = parent.fluids_legend_df.loc[
            (parent.fluids_legend_df["fluid_type"] == fluid_type)
            & (parent.fluids_legend_df["fluid_feature"] == feature)
            & (parent.fluids_legend_df["scenario"] == scenario),
            "color_G",
        ].values[0]
        old_color_B = parent.fluids_legend_df.loc[
            (parent.fluids_legend_df["fluid_type"] == fluid_type)
            & (parent.fluids_legend_df["fluid_feature"] == feature)
            & (parent.fluids_legend_df["scenario"] == scenario),
            "color_B",
        ].values[0]
        color_in = QColor(
            old_color_R, old_color_G, old_color_B
        )  # https://doc.qt.io/qtforpython/PySide2/QtGui/QColor.html#PySide2.QtGui.QColor
        color_out = QColorDialog.getColor(
            initial=color_in, title="Select color"
        )  # https://doc.qt.io/qtforpython/PySide2/QtWidgets/QColorDialog.html#PySide2.QtWidgets.PySide2.QtWidgets.QColorDialog.getColor
        if not color_out.isValid():
            color_out = color_in
        new_color_R = color_out.red()
        new_color_G = color_out.green()
        new_color_B = color_out.blue()
        """Here the query is reversed and modified, dropping the values() method, to allow SETTING the color in the legend."""
        parent.fluids_legend_df.loc[
            (parent.fluids_legend_df["fluid_type"] == fluid_type)
            & (parent.fluids_legend_df["fluid_feature"] == feature)
            & (parent.fluids_legend_df["scenario"] == scenario),
            "color_R",
        ] = new_color_R
        parent.fluids_legend_df.loc[
            (parent.fluids_legend_df["fluid_type"] == fluid_type)
            & (parent.fluids_legend_df["fluid_feature"] == feature)
            & (parent.fluids_legend_df["scenario"] == scenario),
            "color_G",
        ] = new_color_G
        parent.fluids_legend_df.loc[
            (parent.fluids_legend_df["fluid_type"] == fluid_type)
            & (parent.fluids_legend_df["fluid_feature"] == feature)
            & (parent.fluids_legend_df["scenario"] == scenario),
            "color_B",
        ] = new_color_B
        """Update button color."""
        self.sender().setStyleSheet(
            "background-color:rgb({},{},{})".format(
                new_color_R, new_color_G, new_color_B
            )
        )
        """Signal to update actors in windows. This is emitted only for the modified uid under the 'color' key."""
        updated_list = parent.fluids_coll.df.loc[
            (parent.fluids_coll.df["fluid_type"] == fluid_type)
            & (parent.fluids_coll.df["fluid_feature"] == feature)
            & (parent.fluids_coll.df["scenario"] == scenario),
            "uid",
        ].to_list()
        parent.fluid_legend_color_modified_signal.emit(updated_list)
        # self.change_fluid_feature_color(parent) #Update the fluids

    def change_fluid_feature_line_thick(self, parent=None):
        fluid_type = self.sender().fluid_type
        feature = self.sender().feature
        scenario = self.sender().scenario
        line_thick = self.sender().value()
        "Here the query is reversed and modified, dropping the values() method, to allow SETTING the line thickness in the legend"
        parent.fluids_legend_df.loc[
            (parent.fluids_legend_df["fluid_type"] == fluid_type)
            & (parent.fluids_legend_df["fluid_feature"] == feature)
            & (parent.fluids_legend_df["scenario"] == scenario),
            "line_thick",
        ] = line_thick
        """Signal to update actors in windows. This is emitted only for the modified uid under the 'line_thick' key."""
        updated_list = parent.fluids_coll.df.loc[
            (parent.fluids_coll.df["fluid_type"] == fluid_type)
            & (parent.fluids_coll.df["fluid_feature"] == feature)
            & (parent.fluids_coll.df["scenario"] == scenario),
            "uid",
        ].to_list()
        parent.fluid_legend_thick_modified_signal.emit(updated_list)

    def change_fluid_feature_point_size(self, parent=None):
        fluid_type = self.sender().fluid_type
        feature = self.sender().feature
        scenario = self.sender().scenario
        point_size = self.sender().value()
        "Here the query is reversed and modified, dropping the values() method, to allow SETTING the line thickness in the legend"
        parent.fluids_legend_df.loc[
            (parent.fluids_legend_df["fluid_type"] == fluid_type)
            & (parent.fluids_legend_df["fluid_feature"] == feature)
            & (parent.fluids_legend_df["scenario"] == scenario),
            "point_size",
        ] = point_size
        """Signal to update actors in windows. This is emitted only for the modified uid under the 'line_thick' key."""
        updated_list = parent.fluids_coll.df.loc[
            (parent.fluids_coll.df["fluid_type"] == fluid_type)
            & (parent.fluids_coll.df["fluid_feature"] == feature)
            & (parent.fluids_coll.df["scenario"] == scenario),
            "uid",
        ].to_list()
        parent.fluid_legend_point_size_modified_signal.emit(updated_list)

    def change_fluid_feature_opacity(self, parent=None):
        fluid_type = self.sender().fluid_type
        feature = self.sender().feature
        scenario = self.sender().scenario
        opacity = self.sender().value()
        "Here the query is reversed and modified, dropping the values() method, to allow SETTING the line thickness in the legend"
        parent.fluids_legend_df.loc[
            (parent.fluids_legend_df["fluid_type"] == fluid_type)
            & (parent.fluids_legend_df["fluid_feature"] == feature)
            & (parent.fluids_legend_df["scenario"] == scenario),
            "opacity",
        ] = opacity
        """Signal to update actors in windows. This is emitted only for the modified uid under the 'line_thick' key."""
        updated_list = parent.fluids_coll.df.loc[
            (parent.fluids_coll.df["fluid_type"] == fluid_type)
            & (parent.fluids_coll.df["fluid_feature"] == feature)
            & (parent.fluids_coll.df["scenario"] == scenario),
            "uid",
        ].to_list()
        parent.fluid_legend_opacity_modified_signal.emit(updated_list)

    def change_fluid_time(self, parent=None):
        fluid_type = self.sender().fluid_type
        feature = self.sender().feature
        scenario = self.sender().scenario
        fluid_time = self.sender().value()
        parent.fluids_legend_df.loc[
            (parent.fluids_legend_df["fluid_type"] == fluid_type)
            & (parent.fluids_legend_df["fluid_feature"] == feature)
            & (parent.fluids_legend_df["scenario"] == scenario),
            "fluid_time",
        ] = fluid_time
        """Order geological legend entities with descending geological_time values"""
        parent.fluids_legend_df.sort_values(
            by="fluid_time", ascending=True, inplace=True
        )
        """THE FOLLOWING MUST BE CHANGED IN A SORT COMMAND
        UPDATE AT THE MOMENT DOES NOT WORK PROPERLY"""
        # parent.LegendTreeWidget.setSortingEnabled(True)
        # parent.LegendTreeWidget.sortByColumn(7, Qt.AscendingOrder)
        # parent.LegendTreeWidget.setSortingEnabled(False)
        # try:
        #     geol_time = float(self.sender().currentText())
        # except:
        #     geol_time = float('nan')
        #     parent.geol_legend_df.loc[(parent.geol_legend_df['geological_type'] == geo_type) & (parent.geol_legend_df['geological_feature'] == feature) & (parent.geol_legend_df['scenario'] == scenario), "geological_time"] = geol_time
        #     """Order geological legend entities with descending geological_time values"""
        #     parent.geol_legend_df.sort_values(by='geological_time', ascending=True, inplace=True)
        #     self.update_widget(parent=parent)

    def change_background_feature_color(self, parent=None):
        background_type = self.sender().background_type
        feature = self.sender().feature
        """Here we use the same query as above to GET the color from the legend"""
        old_color_R = parent.backgrounds_legend_df.loc[
            (parent.backgrounds_legend_df["background_type"] == background_type)
            & (parent.backgrounds_legend_df["background_feature"] == feature),
            "color_R",
        ].values[0]
        old_color_G = parent.backgrounds_legend_df.loc[
            (parent.backgrounds_legend_df["background_type"] == background_type)
            & (parent.backgrounds_legend_df["background_feature"] == feature),
            "color_G",
        ].values[0]
        old_color_B = parent.backgrounds_legend_df.loc[
            (parent.backgrounds_legend_df["background_type"] == background_type)
            & (parent.backgrounds_legend_df["background_feature"] == feature),
            "color_B",
        ].values[0]
        color_in = QColor(
            old_color_R, old_color_G, old_color_B
        )  # https://doc.qt.io/qtforpython/PySide2/QtGui/QColor.html#PySide2.QtGui.QColor
        color_out = QColorDialog.getColor(
            initial=color_in, title="Select color"
        )  # https://doc.qt.io/qtforpython/PySide2/QtWidgets/QColorDialog.html#PySide2.QtWidgets.PySide2.QtWidgets.QColorDialog.getColor
        if not color_out.isValid():
            color_out = color_in
        new_color_R = color_out.red()
        new_color_G = color_out.green()
        new_color_B = color_out.blue()
        """Here the query is reversed and modified, dropping the values() method, to allow SETTING the color in the legend."""
        parent.backgrounds_legend_df.loc[
            (parent.backgrounds_legend_df["background_type"] == background_type)
            & (parent.backgrounds_legend_df["background_feature"] == feature),
            "color_R",
        ] = new_color_R
        parent.backgrounds_legend_df.loc[
            (parent.backgrounds_legend_df["background_type"] == background_type)
            & (parent.backgrounds_legend_df["background_feature"] == feature),
            "color_G",
        ] = new_color_G
        parent.backgrounds_legend_df.loc[
            (parent.backgrounds_legend_df["background_type"] == background_type)
            & (parent.backgrounds_legend_df["background_feature"] == feature),
            "color_B",
        ] = new_color_B
        """Update button color."""
        self.sender().setStyleSheet(
            "background-color:rgb({},{},{})".format(
                new_color_R, new_color_G, new_color_B
            )
        )
        """Signal to update actors in windows. This is emitted only for the modified uid under the 'color' key."""
        updated_list = parent.backgrounds_coll.df.loc[
            (parent.backgrounds_coll.df["background_type"] == background_type)
            & (parent.backgrounds_coll.df["background_feature"] == feature),
            "uid",
        ].to_list()
        parent.background_legend_color_modified_signal.emit(updated_list)

    def change_background_feature_line_thick(self, parent=None):
        background_type = self.sender().background_type
        feature = self.sender().feature
        line_thick = self.sender().value()
        "Here the query is reversed and modified, dropping the values() method, to allow SETTING the line thickness in the legend"
        parent.backgrounds_legend_df.loc[
            (parent.backgrounds_legend_df["background_type"] == background_type)
            & (parent.backgrounds_legend_df["background_feature"] == feature),
            "line_thick",
        ] = line_thick
        """Signal to update actors in windows. This is emitted only for the modified uid under the 'line_thick' key."""
        updated_list = parent.backgrounds_coll.df.loc[
            (parent.backgrounds_coll.df["background_type"] == background_type)
            & (parent.backgrounds_coll.df["background_feature"] == feature),
            "uid",
        ].to_list()
        parent.background_legend_thick_modified_signal.emit(updated_list)

    def change_background_feature_point_size(self, parent=None):
        background_type = self.sender().background_type
        feature = self.sender().feature
        point_size = self.sender().value()
        "Here the query is reversed and modified, dropping the values() method, to allow SETTING the line thickness in the legend"
        parent.backgrounds_legend_df.loc[
            (parent.backgrounds_legend_df["background_type"] == background_type)
            & (parent.backgrounds_legend_df["background_feature"] == feature),
            "point_size",
        ] = point_size
        """Signal to update actors in windows. This is emitted only for the modified uid under the 'line_thick' key."""
        updated_list = parent.backgrounds_coll.df.loc[
            (parent.backgrounds_coll.df["background_type"] == background_type)
            & (parent.backgrounds_coll.df["background_feature"] == feature),
            "uid",
        ].to_list()
        parent.background_legend_point_size_modified_signal.emit(updated_list)

    def change_background_opacity(self, parent=None):
        background_type = self.sender().background_type
        feature = self.sender().feature
        opacity = self.sender().value()
        "Here the query is reversed and modified, dropping the values() method, to allow SETTING the opacity in the legend"
        parent.backgrounds_legend_df.loc[
            (parent.backgrounds_legend_df["background_type"] == background_type)
            & (parent.backgrounds_legend_df["background_feature"] == feature),
            "opacity",
        ] = opacity
        """Signal to update actors in windows. This is emitted only for the modified uid under the 'line_thick' key."""
        updated_list = parent.backgrounds_coll.df.loc[
            (parent.backgrounds_coll.df["background_type"] == background_type)
            & (parent.backgrounds_coll.df["background_feature"] == feature),
            "uid",
        ].to_list()
        parent.background_legend_opacity_modified_signal.emit(updated_list)

    # def change_geological_sequence(self, parent=None):
    #     geo_type = self.sender().geo_type
    #     feature = self.sender().feature
    #     scenario = self.sender().scenario
    #     geol_seqn = self.sender().currentText()
    #     parent.geol_legend_df.loc[(parent.geol_legend_df['geological_type'] == geo_type) & (parent.geol_legend_df['geological_feature'] == feature) & (parent.geol_legend_df['scenario'] == scenario), "geological_sequence"] = geol_seqn
    #     """THE FOLLOWING MUST BE CHANGED IN A FOR LOOP OVER ALL ITEMS IN COLUMN 7
    #     parent.LegendTreeWidget.setItemWidget(llevel_3, 7, geol_sequence_combo)
    #     UPDATING THE VALUES AS IN
    #     geol_sequence_combo.addItems(parent.geol_legend_df['geological_sequence'].unique())"""
