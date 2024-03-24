import sys
from PySide2 import QtWidgets, QtCore


class ArtistTrackerUi(QtWidgets.QMainWindow):

    def __init__(self):
        super(ArtistTrackerUi, self).__init__()
        self.setup_ui()
        self.show()

    def setup_ui(self):
        # creating WindowTitle
        self.setWindowTitle('Project Tracker ')
        self.resize(1000, 800)
        # self.setMinimumSize(QtCore.QSize(1000, 800))
        # self.setMaximumSize(QtCore.QSize(1000, 800))

        # MainWidget
        main_widget = QtWidgets.QWidget()
        self.setCentralWidget(main_widget)

        # Vertical layout
        main_ver_layout = QtWidgets.QVBoxLayout()

        # Tab Widget
        tabs_widget = QtWidgets.QTabWidget()

        # Tab Main Widget
        project_tab = QtWidgets.QWidget()
        asset_creation_tab = QtWidgets.QWidget()
        asset_tab = QtWidgets.QWidget()
        shots_tab = QtWidgets.QWidget()

        # Horizontal Layout
        prj_tab_lay = QtWidgets.QHBoxLayout()
        ast_creation_tab_lay = QtWidgets.QHBoxLayout()
        asset_tab_lay = QtWidgets.QHBoxLayout()
        shot_tab_lay = QtWidgets.QHBoxLayout()

        # GridLayout
        prj_grid_lay = QtWidgets.QGridLayout()
        ast_creation_grid_lay = QtWidgets.QGridLayout()
        asset_grid_lay = QtWidgets.QGridLayout()
        shot_grid_lay = QtWidgets.QGridLayout()

        # Horizontal Line
        self.ast_HLine = QtWidgets.QFrame()
        self.ast_HLine.setFrameShape(QtWidgets.QFrame.HLine)

        self.shot_HLine = QtWidgets.QFrame()
        self.shot_HLine.setFrameShape(QtWidgets.QFrame.HLine)

        # Labels
        self.prj_name_lbl = QtWidgets.QLabel('Project Name ')
        self.prj_code_lbl = QtWidgets.QLabel('Project Code ')
        self.prj_Client_lbl = QtWidgets.QLabel('Client Name ')
        self.prj_Producer_lbl = QtWidgets.QLabel('Producer Name ')
        self.prj_lineProducer_lbl = QtWidgets.QLabel('LineProducer Name ')
        self.prj_type_lbl = QtWidgets.QLabel('Project Type')
        self.prj_Mandays_lbl = QtWidgets.QLabel('Mandays ')

        self.ast_name_lbl = QtWidgets.QLabel('Asset Name')
        self.ast_type_lbl = QtWidgets.QLabel('Asset Type')

        self.ast_proj_lbl = QtWidgets.QLabel('Projects')
        self.ast_artist_lbl = QtWidgets.QLabel('Artists')

        self.shot_proj_lbl = QtWidgets.QLabel('Projects')
        self.shot_artist_lbl = QtWidgets.QLabel('Artists')

        # Projects Combo Box
        self.prj_Type_cb = QtWidgets.QComboBox()
        self.prj_Type_cb.addItems(['Tv Show', 'Feature Films', 'Test', 'DVD'])
        self.ast_prj_cb = QtWidgets.QComboBox()
        self.ast_artist_cb = QtWidgets.QComboBox()

        self.shot_prj_cb = QtWidgets.QComboBox()
        self.shot_artist_cb = QtWidgets.QComboBox()

        # Assets Tree Widget
        self.ast_tree_widget = QtWidgets.QTreeWidget()
        self.ast_tree_widget.setSortingEnabled(True)
        self.ast_tree_widget.setAlternatingRowColors(True)
        self.ast_tree_widget.setColumnCount(9)
        self.ast_tree_widget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.ast_tree_widget.setHeaderLabels(
            ['AssetName', 'AssetType', 'Dept', 'Stage', 'Status', 'StartDate', 'EndDate', 'UploadDate', 'Mandays'])

        # shots Tree Widget
        self.shot_tree_widget = QtWidgets.QTreeWidget()
        self.shot_tree_widget.setSortingEnabled(True)
        self.shot_tree_widget.setAlternatingRowColors(True)
        self.shot_tree_widget.setColumnCount(10)
        self.shot_tree_widget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.shot_tree_widget.setHeaderLabels(
            ['Episode', 'Seq', 'Shot', 'Dept', 'Stage', 'Status', 'StartDate', 'EndDate', 'UploadDate', 'Mandays'])

        # Line Edit
        self.prj_name_LineEdit = QtWidgets.QLineEdit()
        self.prj_code_LineEdit = QtWidgets.QLineEdit()
        self.prj_client_LineEdit = QtWidgets.QLineEdit()
        self.prj_producer_LineEdit = QtWidgets.QLineEdit()
        self.prj_lineProducer_LineEdit = QtWidgets.QLineEdit()
        self.prj_Mandays_LineEdit = QtWidgets.QLineEdit()

        self.asset_name_LineEdit = QtWidgets.QLineEdit()
        self.asset_type_LineEdit = QtWidgets.QLineEdit()

        # Push Buttons
        self.PrjCreation_btn = QtWidgets.QPushButton('Create Project')
        self.PrjUpdate_btn = QtWidgets.QPushButton('Update Project')

        self.AstCreation_btn = QtWidgets.QPushButton('Create Asset')

        # Project Creation Tab Connections
        prj_tab_lay.addLayout(prj_grid_lay)
        prj_grid_lay.addWidget(self.prj_name_lbl, 0, 0)
        prj_grid_lay.addWidget(self.prj_name_LineEdit, 0, 1)
        prj_grid_lay.addWidget(self.prj_code_lbl, 1, 0)
        prj_grid_lay.addWidget(self.prj_code_LineEdit, 1, 1)
        prj_grid_lay.addWidget(self.prj_Client_lbl, 2, 0)
        prj_grid_lay.addWidget(self.prj_client_LineEdit, 2, 1)
        prj_grid_lay.addWidget(self.prj_Producer_lbl, 3, 0)
        prj_grid_lay.addWidget(self.prj_producer_LineEdit, 3, 1)
        prj_grid_lay.addWidget(self.prj_lineProducer_lbl, 4, 0)
        prj_grid_lay.addWidget(self.prj_lineProducer_LineEdit, 4, 1)
        prj_grid_lay.addWidget(self.prj_type_lbl, 5, 0)
        prj_grid_lay.addWidget(self.prj_Type_cb, 5, 1)
        prj_grid_lay.addWidget(self.prj_Mandays_lbl, 6, 0)
        prj_grid_lay.addWidget(self.prj_Mandays_LineEdit, 6, 1)
        prj_grid_lay.addWidget(self.PrjCreation_btn, 7, 0, 1, -1)
        prj_grid_lay.addWidget(self.PrjUpdate_btn, 8, 0, 1, -1)
        project_tab.setLayout(prj_tab_lay)

        # Asset Creation Tab Connections

        ast_creation_tab_lay.addLayout(ast_creation_grid_lay)
        ast_creation_grid_lay.addWidget(self.ast_name_lbl, 0, 0)
        ast_creation_grid_lay.addWidget(self.asset_name_LineEdit, 0, 1)
        ast_creation_grid_lay.addWidget(self.ast_type_lbl, 1, 0)
        ast_creation_grid_lay.addWidget(self.asset_type_LineEdit, 1, 1)
        ast_creation_grid_lay.addWidget(self.AstCreation_btn, 2, 0, 1, -1)
        asset_creation_tab.setLayout(ast_creation_tab_lay)

        # Asset Tab Connections
        asset_tab_lay.addLayout(asset_grid_lay)
        asset_grid_lay.addWidget(self.ast_proj_lbl, 0, 0)
        asset_grid_lay.addWidget(self.ast_prj_cb, 0, 1)
        asset_grid_lay.addWidget(self.ast_proj_lbl, 0, 2)
        asset_grid_lay.addWidget(self.ast_artist_lbl, 0, 3)
        asset_grid_lay.addWidget(self.ast_artist_cb, 0, 4)
        asset_grid_lay.addWidget(self.ast_HLine, 1, 0, 1, -1)
        asset_grid_lay.addWidget(self.ast_tree_widget, 2, 0, 1, -1)
        asset_tab.setLayout(asset_tab_lay)

        # Shot Tab Connections
        shot_tab_lay.addLayout(shot_grid_lay)
        shot_grid_lay.addWidget(self.shot_proj_lbl, 0, 0)
        shot_grid_lay.addWidget(self.shot_prj_cb, 0, 1)
        shot_grid_lay.addWidget(self.shot_proj_lbl, 0, 2)
        shot_grid_lay.addWidget(self.shot_artist_lbl, 0, 3)
        shot_grid_lay.addWidget(self.shot_artist_cb, 0, 4)
        shot_grid_lay.addWidget(self.shot_HLine, 1, 0, 1, -1)
        shot_grid_lay.addWidget(self.shot_tree_widget, 2, 0, 1, -1)
        shots_tab.setLayout(shot_tab_lay)

        tabs_widget.addTab(project_tab, 'ProjectCreation')
        tabs_widget.addTab(asset_creation_tab, 'AssetCreation')
        tabs_widget.addTab(asset_tab, 'Assets')
        tabs_widget.addTab(shots_tab, 'Shots')

        # Adding widgets to Main layout
        main_ver_layout.addWidget(tabs_widget)
        main_widget.setLayout(main_ver_layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet("QWidget { background-color :lightblue;}")
    main = ArtistTrackerUi()
    main.show()
    sys.exit(app.exec_())
