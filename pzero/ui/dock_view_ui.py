# -*- coding: utf-8 -*-

# QDockWidget implementation generated from reading ui file 'dock_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QDockWidget(object):
    def setupUi(self, QDockWidget):
        QDockWidget.setObjectName("DockWidget")
        QDockWidget.resize(1280, 800)
        self.verticalLayoutWidget = QtWidgets.QWidget(QDockWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 1251, 741))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.centralWidget = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.centralWidget.setContentsMargins(11, 11, 11, 11)
        self.centralWidget.setObjectName("centralWidget")
        self.splitter = QtWidgets.QSplitter(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setMinimumSize(QtCore.QSize(10, 10))
        self.splitter.setBaseSize(QtCore.QSize(10, 10))
        self.splitter.setLineWidth(0)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.toolBox_2 = QtWidgets.QToolBox(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.toolBox_2.sizePolicy().hasHeightForWidth())
        self.toolBox_2.setSizePolicy(sizePolicy)
        self.toolBox_2.setMinimumSize(QtCore.QSize(274, 534))
        self.toolBox_2.setBaseSize(QtCore.QSize(274, 534))
        self.toolBox_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toolBox_2.setObjectName("toolBox_2")
        self.GeologyTreePage_2 = QtWidgets.QWidget()
        self.GeologyTreePage_2.setGeometry(QtCore.QRect(0, 0, 278, 347))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.GeologyTreePage_2.sizePolicy().hasHeightForWidth()
        )
        self.GeologyTreePage_2.setSizePolicy(sizePolicy)
        self.GeologyTreePage_2.setMinimumSize(QtCore.QSize(10, 10))
        self.GeologyTreePage_2.setBaseSize(QtCore.QSize(10, 10))
        self.GeologyTreePage_2.setObjectName("GeologyTreePage_2")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.GeologyTreePage_2)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.GeologyTreeWidget = QtWidgets.QTreeWidget(self.GeologyTreePage_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.GeologyTreeWidget.sizePolicy().hasHeightForWidth()
        )
        self.GeologyTreeWidget.setSizePolicy(sizePolicy)
        self.GeologyTreeWidget.setMinimumSize(QtCore.QSize(10, 10))
        self.GeologyTreeWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.GeologyTreeWidget.setBaseSize(QtCore.QSize(10, 10))
        self.GeologyTreeWidget.setObjectName("GeologyTreeWidget")
        self.GeologyTreeWidget.headerItem().setText(0, "1")
        self.verticalLayout_14.addWidget(self.GeologyTreeWidget)
        self.toolBox_2.addItem(self.GeologyTreePage_2, "")
        self.TopologyTreePage_2 = QtWidgets.QWidget()
        self.TopologyTreePage_2.setGeometry(QtCore.QRect(0, 0, 278, 347))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.TopologyTreePage_2.sizePolicy().hasHeightForWidth()
        )
        self.TopologyTreePage_2.setSizePolicy(sizePolicy)
        self.TopologyTreePage_2.setMinimumSize(QtCore.QSize(10, 10))
        self.TopologyTreePage_2.setBaseSize(QtCore.QSize(10, 10))
        self.TopologyTreePage_2.setObjectName("TopologyTreePage_2")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.TopologyTreePage_2)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.TopologyTreeWidget = QtWidgets.QTreeWidget(self.TopologyTreePage_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.TopologyTreeWidget.sizePolicy().hasHeightForWidth()
        )
        self.TopologyTreeWidget.setSizePolicy(sizePolicy)
        self.TopologyTreeWidget.setMinimumSize(QtCore.QSize(10, 10))
        self.TopologyTreeWidget.setBaseSize(QtCore.QSize(10, 10))
        self.TopologyTreeWidget.setObjectName("TopologyTreeWidget")
        self.TopologyTreeWidget.headerItem().setText(0, "1")
        self.verticalLayout_15.addWidget(self.TopologyTreeWidget)
        self.toolBox_2.addItem(self.TopologyTreePage_2, "")
        self.XSectionListPage_2 = QtWidgets.QWidget()
        self.XSectionListPage_2.setGeometry(QtCore.QRect(0, 0, 278, 347))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.XSectionListPage_2.sizePolicy().hasHeightForWidth()
        )
        self.XSectionListPage_2.setSizePolicy(sizePolicy)
        self.XSectionListPage_2.setMinimumSize(QtCore.QSize(10, 10))
        self.XSectionListPage_2.setBaseSize(QtCore.QSize(10, 10))
        self.XSectionListPage_2.setObjectName("XSectionListPage_2")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.XSectionListPage_2)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.XSectionTreeWidget = QtWidgets.QTreeWidget(self.XSectionListPage_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.XSectionTreeWidget.sizePolicy().hasHeightForWidth()
        )
        self.XSectionTreeWidget.setSizePolicy(sizePolicy)
        self.XSectionTreeWidget.setMinimumSize(QtCore.QSize(10, 10))
        self.XSectionTreeWidget.setBaseSize(QtCore.QSize(10, 10))
        self.XSectionTreeWidget.setTabKeyNavigation(True)
        self.XSectionTreeWidget.setDragDropOverwriteMode(True)
        self.XSectionTreeWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.ExtendedSelection
        )
        self.XSectionTreeWidget.setHorizontalScrollMode(
            QtWidgets.QAbstractItemView.ScrollPerItem
        )
        self.XSectionTreeWidget.setAutoExpandDelay(-1)
        self.XSectionTreeWidget.setObjectName("XSectionTreeWidget")
        self.XSectionTreeWidget.headerItem().setText(0, "1")
        self.verticalLayout_16.addWidget(self.XSectionTreeWidget)
        self.toolBox_2.addItem(self.XSectionListPage_2, "")
        self.BoundariesPage_2 = QtWidgets.QWidget()
        self.BoundariesPage_2.setGeometry(QtCore.QRect(0, 0, 278, 347))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.BoundariesPage_2.sizePolicy().hasHeightForWidth()
        )
        self.BoundariesPage_2.setSizePolicy(sizePolicy)
        self.BoundariesPage_2.setObjectName("BoundariesPage_2")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.BoundariesPage_2)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.BoundariesTableWidget = QtWidgets.QTableWidget(self.BoundariesPage_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.BoundariesTableWidget.sizePolicy().hasHeightForWidth()
        )
        self.BoundariesTableWidget.setSizePolicy(sizePolicy)
        self.BoundariesTableWidget.setMinimumSize(QtCore.QSize(10, 10))
        self.BoundariesTableWidget.setBaseSize(QtCore.QSize(10, 10))
        self.BoundariesTableWidget.setObjectName("BoundariesTableWidget")
        self.BoundariesTableWidget.setColumnCount(0)
        self.BoundariesTableWidget.setRowCount(0)
        self.verticalLayout_17.addWidget(self.BoundariesTableWidget)
        self.toolBox_2.addItem(self.BoundariesPage_2, "")
        self.Mesh3DPage_2 = QtWidgets.QWidget()
        self.Mesh3DPage_2.setGeometry(QtCore.QRect(0, 0, 278, 347))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.Mesh3DPage_2.sizePolicy().hasHeightForWidth())
        self.Mesh3DPage_2.setSizePolicy(sizePolicy)
        self.Mesh3DPage_2.setMinimumSize(QtCore.QSize(10, 10))
        self.Mesh3DPage_2.setBaseSize(QtCore.QSize(10, 10))
        self.Mesh3DPage_2.setObjectName("Mesh3DPage_2")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.Mesh3DPage_2)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.Mesh3DTableWidget = QtWidgets.QTableWidget(self.Mesh3DPage_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.Mesh3DTableWidget.sizePolicy().hasHeightForWidth()
        )
        self.Mesh3DTableWidget.setSizePolicy(sizePolicy)
        self.Mesh3DTableWidget.setMinimumSize(QtCore.QSize(10, 10))
        self.Mesh3DTableWidget.setBaseSize(QtCore.QSize(10, 10))
        self.Mesh3DTableWidget.setObjectName("Mesh3DTableWidget")
        self.Mesh3DTableWidget.setColumnCount(0)
        self.Mesh3DTableWidget.setRowCount(0)
        self.verticalLayout_18.addWidget(self.Mesh3DTableWidget)
        self.toolBox_2.addItem(self.Mesh3DPage_2, "")
        self.DOMsPage_2 = QtWidgets.QWidget()
        self.DOMsPage_2.setGeometry(QtCore.QRect(0, 0, 278, 347))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.DOMsPage_2.sizePolicy().hasHeightForWidth())
        self.DOMsPage_2.setSizePolicy(sizePolicy)
        self.DOMsPage_2.setMinimumSize(QtCore.QSize(10, 10))
        self.DOMsPage_2.setBaseSize(QtCore.QSize(10, 10))
        self.DOMsPage_2.setObjectName("DOMsPage_2")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.DOMsPage_2)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.DOMsTableWidget = QtWidgets.QTableWidget(self.DOMsPage_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.DOMsTableWidget.sizePolicy().hasHeightForWidth()
        )
        self.DOMsTableWidget.setSizePolicy(sizePolicy)
        self.DOMsTableWidget.setMinimumSize(QtCore.QSize(10, 10))
        self.DOMsTableWidget.setBaseSize(QtCore.QSize(10, 10))
        self.DOMsTableWidget.setObjectName("DOMsTableWidget")
        self.DOMsTableWidget.setColumnCount(0)
        self.DOMsTableWidget.setRowCount(0)
        self.verticalLayout_19.addWidget(self.DOMsTableWidget)
        self.toolBox_2.addItem(self.DOMsPage_2, "")
        self.WellsPage_2 = QtWidgets.QWidget()
        self.WellsPage_2.setGeometry(QtCore.QRect(0, 0, 278, 347))
        self.WellsPage_2.setObjectName("WellsPage_2")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.WellsPage_2)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.WellsTreeWidget = QtWidgets.QTreeWidget(self.WellsPage_2)
        self.WellsTreeWidget.setObjectName("WellsTreeWidget")
        self.WellsTreeWidget.headerItem().setText(0, "1")
        self.verticalLayout_20.addWidget(self.WellsTreeWidget)
        self.toolBox_2.addItem(self.WellsPage_2, "")
        self.FluidsTreePage_2 = QtWidgets.QWidget()
        self.FluidsTreePage_2.setGeometry(QtCore.QRect(0, 0, 278, 347))
        self.FluidsTreePage_2.setObjectName("FluidsTreePage_2")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.FluidsTreePage_2)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.FluidsTreeWidget = QtWidgets.QTreeWidget(self.FluidsTreePage_2)
        self.FluidsTreeWidget.setObjectName("FluidsTreeWidget")
        self.FluidsTreeWidget.headerItem().setText(0, "1")
        self.verticalLayout_21.addWidget(self.FluidsTreeWidget)
        self.toolBox_2.addItem(self.FluidsTreePage_2, "")
        self.FluidsTopologyTree_2 = QtWidgets.QWidget()
        self.FluidsTopologyTree_2.setGeometry(QtCore.QRect(0, 0, 278, 347))
        self.FluidsTopologyTree_2.setObjectName("FluidsTopologyTree_2")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.FluidsTopologyTree_2)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.FluidsTopologyTreeWidget = QtWidgets.QTreeWidget(self.FluidsTopologyTree_2)
        self.FluidsTopologyTreeWidget.setObjectName("FluidsTopologyTreeWidget")
        self.FluidsTopologyTreeWidget.headerItem().setText(0, "1")
        self.verticalLayout_22.addWidget(self.FluidsTopologyTreeWidget)
        self.toolBox_2.addItem(self.FluidsTopologyTree_2, "")
        self.BackgroundsTreePage_2 = QtWidgets.QWidget()
        self.BackgroundsTreePage_2.setGeometry(QtCore.QRect(0, 0, 278, 347))
        self.BackgroundsTreePage_2.setObjectName("BackgroundsTreePage_2")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.BackgroundsTreePage_2)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.BackgroundsTreeWidget = QtWidgets.QTreeWidget(self.BackgroundsTreePage_2)
        self.BackgroundsTreeWidget.setObjectName("BackgroundsTreeWidget")
        self.BackgroundsTreeWidget.headerItem().setText(0, "1")
        self.verticalLayout_23.addWidget(self.BackgroundsTreeWidget)
        self.toolBox_2.addItem(self.BackgroundsTreePage_2, "")
        self.BackgroundsTopologyTree_2 = QtWidgets.QWidget()
        self.BackgroundsTopologyTree_2.setGeometry(QtCore.QRect(0, 0, 278, 347))
        self.BackgroundsTopologyTree_2.setObjectName("BackgroundsTopologyTree_2")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.BackgroundsTopologyTree_2)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.BackgroundsTopologyTreeWidget = QtWidgets.QTreeWidget(
            self.BackgroundsTopologyTree_2
        )
        self.BackgroundsTopologyTreeWidget.setObjectName(
            "BackgroundsTopologyTreeWidget"
        )
        self.BackgroundsTopologyTreeWidget.headerItem().setText(0, "1")
        self.verticalLayout_24.addWidget(self.BackgroundsTopologyTreeWidget)
        self.toolBox_2.addItem(self.BackgroundsTopologyTree_2, "")
        self.ImagesPage_2 = QtWidgets.QWidget()
        self.ImagesPage_2.setGeometry(QtCore.QRect(0, 0, 278, 347))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.ImagesPage_2.sizePolicy().hasHeightForWidth())
        self.ImagesPage_2.setSizePolicy(sizePolicy)
        self.ImagesPage_2.setMinimumSize(QtCore.QSize(10, 10))
        self.ImagesPage_2.setBaseSize(QtCore.QSize(10, 10))
        self.ImagesPage_2.setObjectName("ImagesPage_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.ImagesPage_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ImagesTableWidget = QtWidgets.QTableWidget(self.ImagesPage_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.ImagesTableWidget.sizePolicy().hasHeightForWidth()
        )
        self.ImagesTableWidget.setSizePolicy(sizePolicy)
        self.ImagesTableWidget.setMinimumSize(QtCore.QSize(10, 10))
        self.ImagesTableWidget.setBaseSize(QtCore.QSize(10, 10))
        self.ImagesTableWidget.setObjectName("ImagesTableWidget")
        self.ImagesTableWidget.setColumnCount(0)
        self.ImagesTableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.ImagesTableWidget)
        self.toolBox_2.addItem(self.ImagesPage_2, "")
        self.ViewFrame = QtWidgets.QFrame(self.splitter)
        self.ViewFrame.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.ViewFrame.sizePolicy().hasHeightForWidth())
        self.ViewFrame.setSizePolicy(sizePolicy)
        self.ViewFrame.setMinimumSize(QtCore.QSize(10, 10))
        self.ViewFrame.setBaseSize(QtCore.QSize(10, 10))
        self.ViewFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ViewFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ViewFrame.setLineWidth(0)
        self.ViewFrame.setObjectName("ViewFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.ViewFrame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ViewFrameLayout = QtWidgets.QVBoxLayout()
        self.ViewFrameLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.ViewFrameLayout.setContentsMargins(4, 4, 4, 4)
        self.ViewFrameLayout.setSpacing(8)
        self.ViewFrameLayout.setObjectName("ViewFrameLayout")
        self.horizontalLayout_2.addLayout(self.ViewFrameLayout)
        self.centralWidget.addWidget(self.splitter)
        self.menubar = QtWidgets.QMenuBar(QDockWidget)
        self.menubar.setGeometry(10, 20, 20, 1250)
        self.menubar.setObjectName("menubar")

        self.actionClose = QtWidgets.QAction(QDockWidget)
        self.actionClose.setObjectName("actionClose")
        self.actionBase_Tool = QtWidgets.QAction(QDockWidget)
        self.actionBase_Tool.setObjectName("actionBase_Tool")
        self.actionFilters = QtWidgets.QAction(QDockWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.actionFilters.setFont(font)
        self.actionFilters.setObjectName("actionFilters")
        self.actionSurface_densityf = QtWidgets.QAction(QDockWidget)
        self.actionSurface_densityf.setObjectName("actionSurface_densityf")
        self.actionRoughnessf = QtWidgets.QAction(QDockWidget)
        self.actionRoughnessf.setObjectName("actionRoughnessf")
        self.actionCurvaturef = QtWidgets.QAction(QDockWidget)
        self.actionCurvaturef.setObjectName("actionCurvaturef")
        self.actionNormalsf = QtWidgets.QAction(QDockWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.actionNormalsf.setFont(font)
        self.actionNormalsf.setObjectName("actionNormalsf")
        self.actionCalculate_normals = QtWidgets.QAction(QDockWidget)
        self.actionCalculate_normals.setObjectName("actionCalculate_normals")
        self.actionNormals_to_DDR = QtWidgets.QAction(QDockWidget)
        self.actionNormals_to_DDR.setObjectName("actionNormals_to_DDR")
        self.actionPickers = QtWidgets.QAction(QDockWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.actionPickers.setFont(font)
        self.actionPickers.setObjectName("actionPickers")
        self.actionManual_picking = QtWidgets.QAction(QDockWidget)
        self.actionManual_picking.setObjectName("actionManual_picking")
        self.actionThresholdf = QtWidgets.QAction(QDockWidget)
        self.actionThresholdf.setObjectName("actionThresholdf")
        self.actionSegment = QtWidgets.QAction(QDockWidget)
        self.actionSegment.setObjectName("actionSegment")
        self.actionPick = QtWidgets.QAction(QDockWidget)
        self.actionPick.setObjectName("actionPick")
        self.actionFacets = QtWidgets.QAction(QDockWidget)
        self.actionFacets.setObjectName("actionFacets")
        self.actionCalibration = QtWidgets.QAction(QDockWidget)
        self.actionCalibration.setObjectName("actionCalibration")
        self.actionManualInner = QtWidgets.QAction(QDockWidget)
        self.actionManualInner.setObjectName("actionManualInner")
        self.actionManualOuter = QtWidgets.QAction(QDockWidget)
        self.actionManualOuter.setObjectName("actionManualOuter")
        self.actionManualBoth = QtWidgets.QAction(QDockWidget)
        self.actionManualBoth.setObjectName("actionManualBoth")

        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuAutomatic_segmentation = QtWidgets.QMenu(self.menuTools)
        self.menuAutomatic_segmentation.setObjectName("menuAutomatic_segmentation")
        self.menuManual = QtWidgets.QMenu(self.menuTools)
        self.menuManual.setObjectName("menuManual")
        self.menuBaseView = QtWidgets.QMenu(self.menubar)
        self.menuBaseView.setObjectName("menuBaseView")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")

        self.menuWindow.addAction(self.actionClose)
        self.menuAutomatic_segmentation.addAction(self.actionSegment)
        self.menuAutomatic_segmentation.addAction(self.actionPick)
        self.menuAutomatic_segmentation.addAction(self.actionFacets)
        self.menuManual.addAction(self.actionManualInner)
        self.menuManual.addAction(self.actionManualOuter)
        self.menuManual.addAction(self.actionManualBoth)
        self.menuTools.addAction(self.actionFilters)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionSurface_densityf)
        self.menuTools.addAction(self.actionRoughnessf)
        self.menuTools.addAction(self.actionCurvaturef)
        self.menuTools.addAction(self.actionThresholdf)
        self.menuTools.addAction(self.menuManual.menuAction())
        self.menuTools.addAction(self.actionNormalsf)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionCalculate_normals)
        self.menuTools.addAction(self.actionNormals_to_DDR)
        self.menuTools.addAction(self.actionPickers)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionCalibration)
        self.menuTools.addAction(self.actionManual_picking)
        self.menuTools.addAction(self.menuAutomatic_segmentation.menuAction())
        self.menubar.addAction(self.menuBaseView.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.move((QtCore.QPoint(0, 30)))

        self.retranslateUi(QDockWidget)
        self.toolBox_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(QDockWidget)

    def retranslateUi(self, QDockWidget):
        _translate = QtCore.QCoreApplication.translate
        QDockWidget.setWindowTitle(_translate("QDockWidget", "QDockWidget"))
        self.toolBox_2.setItemText(
            self.toolBox_2.indexOf(self.GeologyTreePage_2),
            _translate("QDockWidget", "Geology > Geology Tree"),
        )
        self.toolBox_2.setItemText(
            self.toolBox_2.indexOf(self.TopologyTreePage_2),
            _translate("QDockWidget", "Geology > Topology Tree"),
        )
        self.toolBox_2.setItemText(
            self.toolBox_2.indexOf(self.XSectionListPage_2),
            _translate("QDockWidget", "X Section"),
        )
        self.toolBox_2.setItemText(
            self.toolBox_2.indexOf(self.BoundariesPage_2),
            _translate("QDockWidget", "Boundaries"),
        )
        self.toolBox_2.setItemText(
            self.toolBox_2.indexOf(self.Mesh3DPage_2),
            _translate("QDockWidget", "3D Meshes and Grids"),
        )
        self.toolBox_2.setItemText(
            self.toolBox_2.indexOf(self.DOMsPage_2),
            _translate("QDockWidget", "DEMs and DOMs"),
        )
        self.toolBox_2.setItemText(
            self.toolBox_2.indexOf(self.WellsPage_2), _translate("QDockWidget", "Wells")
        )
        self.toolBox_2.setItemText(
            self.toolBox_2.indexOf(self.FluidsTreePage_2),
            _translate("QDockWidget", "Fluids > Fluids Tree"),
        )
        self.toolBox_2.setItemText(
            self.toolBox_2.indexOf(self.FluidsTopologyTree_2),
            _translate("QDockWidget", "Fluids > Topology Tree"),
        )
        self.toolBox_2.setItemText(
            self.toolBox_2.indexOf(self.BackgroundsTreePage_2),
            _translate("QDockWidget", "Background data > Backgrounds tree"),
        )
        self.toolBox_2.setItemText(
            self.toolBox_2.indexOf(self.BackgroundsTopologyTree_2),
            _translate("QDockWidget", "Background data > Topology tree"),
        )
        self.toolBox_2.setItemText(
            self.toolBox_2.indexOf(self.ImagesPage_2),
            _translate("QDockWidget", "Images"),
        )

        self.menuBaseView.setTitle(_translate("QDockWidget", "Base View"))
        self.menuHelp.setTitle(_translate("QDockWidget", "Help"))
        self.menuWindow.setTitle(_translate("QDockWidget", "Window"))
        self.menuTools.setTitle(_translate("QDockWidget", "Tools"))
        self.menuAutomatic_segmentation.setTitle(
            _translate("QDockWidget", "Automatic segmentation")
        )
        self.menuManual.setTitle(_translate("QDockWidget", "Manual"))
        self.actionClose.setText(_translate("QDockWidget", "Close Window"))
        self.actionBase_Tool.setText(_translate("QDockWidget", "Base Tool"))
        self.actionFilters.setText(_translate("QDockWidget", "Filters"))
        self.actionSurface_densityf.setText(
            _translate("QDockWidget", "Surface density")
        )
        self.actionRoughnessf.setText(_translate("QDockWidget", "Roughness"))
        self.actionCurvaturef.setText(_translate("QDockWidget", "Curvature"))
        self.actionNormalsf.setText(_translate("QDockWidget", "Normals"))
        self.actionCalculate_normals.setText(
            _translate("QDockWidget", "Calculate normals")
        )
        self.actionNormals_to_DDR.setText(
            _translate("QDockWidget", "Normals to Dip/Dip direction")
        )
        self.actionPickers.setText(_translate("QDockWidget", "Pickers"))
        self.actionManual_picking.setText(_translate("QDockWidget", "Manual picking"))
        self.actionThresholdf.setText(_translate("QDockWidget", "Threshold"))
        self.actionSegment.setText(_translate("QDockWidget", "Segment"))
        self.actionPick.setText(_translate("QDockWidget", "Pick"))
        self.actionFacets.setText(_translate("QDockWidget", "Facets"))
        self.actionCalibration.setText(_translate("QDockWidget", "Calibration"))
        self.actionManualInner.setText(_translate("QDockWidget", "Inner"))
        self.actionManualOuter.setText(_translate("QDockWidget", "Outer"))
        self.actionManualBoth.setText(_translate("QDockWidget", "Both"))
