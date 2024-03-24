
import sys
from PySide2 import QtWidgets,QtCore


class ArtistTrackerUi(QtWidgets.QMainWindow):

    def __init__(self):
        super(ArtistTrackerUi, self).__init__()
        self.setup_ui()
        self.show()

    def setup_ui(self):

        # creating WindowTitle
        self.setWindowTitle('Artist Assignment Tracker ')
        self.resize(1000,800)
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
        asset_tab = QtWidgets.QWidget()
        shots_tab = QtWidgets.QWidget()

        # Horizontal Layout
        asset_tab_lay = QtWidgets.QHBoxLayout()
        shot_tab_lay = QtWidgets.QHBoxLayout()

        # GridLayout
        asset_grid_lay = QtWidgets.QGridLayout()
        shot_grid_lay = QtWidgets.QGridLayout()

        # Horizontal Line
        self.ast_HLine = QtWidgets.QFrame()
        self.ast_HLine.setFrameShape(QtWidgets.QFrame.HLine)

        self.shot_HLine = QtWidgets.QFrame()
        self.shot_HLine.setFrameShape(QtWidgets.QFrame.HLine)

        # Labels
        self.ast_proj_lbl = QtWidgets.QLabel('Projects')
        self.ast_artist_lbl = QtWidgets.QLabel('Artists')

        self.shot_proj_lbl = QtWidgets.QLabel('Projects')
        self.shot_artist_lbl = QtWidgets.QLabel('Artists')

        # Projects Combo Box
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
        self.ast_tree_widget.setHeaderLabels(['AssetName', 'AssetType','Dept','Stage','Status','StartDate','EndDate','UploadDate','Mandays'])

        # shots Tree Widget
        self.shot_tree_widget = QtWidgets.QTreeWidget()
        self.shot_tree_widget.setSortingEnabled(True)
        self.shot_tree_widget.setAlternatingRowColors(True)
        self.shot_tree_widget.setColumnCount(10)
        self.shot_tree_widget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.shot_tree_widget.setHeaderLabels(['Episode', 'Seq', 'Shot', 'Dept', 'Stage','Status','StartDate', 'EndDate', 'UploadDate', 'Mandays'])


        # Asset Tab Connections
        asset_tab_lay.addLayout(asset_grid_lay)
        asset_grid_lay.addWidget(self.ast_proj_lbl,0,0)
        asset_grid_lay.addWidget(self.ast_prj_cb,0,1)
        asset_grid_lay.addWidget(self.ast_proj_lbl,0,2)
        asset_grid_lay.addWidget(self.ast_artist_lbl,0,3)
        asset_grid_lay.addWidget(self.ast_artist_cb,0,4)
        asset_grid_lay.addWidget(self.ast_HLine,1,0,1,-1)
        asset_grid_lay.addWidget(self.ast_tree_widget,2,0,1,-1)
        asset_tab.setLayout(asset_tab_lay)

        # Shot Tab Connections
        shot_tab_lay.addLayout(shot_grid_lay)
        shot_grid_lay.addWidget(self.shot_proj_lbl, 0, 0)
        shot_grid_lay.addWidget(self.shot_prj_cb, 0, 1)
        shot_grid_lay.addWidget(self.shot_proj_lbl, 0, 2)
        shot_grid_lay.addWidget(self.shot_artist_lbl, 0, 3)
        shot_grid_lay.addWidget(self.shot_artist_cb, 0, 4)
        shot_grid_lay.addWidget(self.shot_HLine, 1, 0,1,-1)
        shot_grid_lay.addWidget(self.shot_tree_widget, 2, 0, 1, -1)
        shots_tab.setLayout(shot_tab_lay)

        tabs_widget.addTab(asset_tab, 'Assets')
        tabs_widget.addTab(shots_tab, 'Shots')

        # Adding widgets to Main layout
        main_ver_layout.addWidget(tabs_widget)
        main_widget.setLayout(main_ver_layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet("QWidget { background-color :lightgreen;}")
    main = ArtistTrackerUi()
    main.show()
    sys.exit(app.exec_())
