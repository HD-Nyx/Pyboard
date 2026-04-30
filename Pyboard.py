from PySide6.QtWidgets import QApplication, QHBoxLayout, QListWidget, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QInputDialog
from PySide6.QtCore import Qt

from Assets.Scripts.Soundboard import CreateSoundboard, DeleteSoundboard, GetSoundboards
from Assets.Scripts import InstallVB_Cable

import sounddevice
import sys


print("Devices founded from sounddevice ↓ ('>' = Input | '<' = Output) \n")
print(sounddevice.query_devices())

class PyBoard(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyBoard')
        self.resize(1200, 800)
        self._BuildUi()
        self._LoadSoundboards()

    def _BuildUi(self):
        # Main Area
        CentralArea = QWidget()
        CentralArea.setStyleSheet("background: transparent;")
        MainLayout = QHBoxLayout(CentralArea)
        MainLayout.setContentsMargins(0, 0, 0, 0)
        MainLayout.setSpacing(0)

        # Sidebar
        Sidebar = QWidget()
        Sidebar.setFixedWidth(200)
        SidebarLayout = QVBoxLayout(Sidebar)
        SidebarLayout.setContentsMargins(8, 8, 8, 8)

        self.SoundboardList = QListWidget()
        self.SoundboardList.setStyleSheet("background: transparent; color: white; border: none;")

        self.NewBoardButton = QPushButton("+ New Board")
        self.NewBoardButton.setStyleSheet("color: white;")
        self.NewBoardButton.clicked.connect(self._NewSoundboard)

        self.DeleteBoardButton = QPushButton("- Delete Board")
        self.DeleteBoardButton.setStyleSheet("color: white;")
        self.DeleteBoardButton.clicked.connect(self._DeleteSoundboard)

        SidebarLayout.addWidget(self.SoundboardList)
        SidebarLayout.addWidget(self.NewBoardButton)
        SidebarLayout.addWidget(self.DeleteBoardButton)

        # Right Panel
        self.RightPanel = QLabel("Select a soundboard")
        self.RightPanel.setAlignment(Qt.AlignCenter)
        self.RightPanel.setStyleSheet("background-color: rgba(20, 20, 20, 160); color: white;")

        MainLayout.addWidget(Sidebar)
        MainLayout.addWidget(self.RightPanel, stretch=1)

        self.setCentralWidget(CentralArea)

    # Soundboard functions in class
    def _LoadSoundboards(self):
        self.SoundboardList.clear()
        self.SoundboardList.addItems(GetSoundboards())

    def _NewSoundboard(self):
        QApplication.beep()
        Name, Ok = QInputDialog.getText(self, "New Soundboard", "Enter a name:")

        if Ok and Name:
            CreateSoundboard(Name)
            self._LoadSoundboards()

    def _DeleteSoundboard(self):
        Current = self.SoundboardList.currentItem()

        if Current:
            DeleteSoundboard(Current.text())
            self._LoadSoundboards()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    Window = PyBoard()
    Window.show()
    sys.exit(App.exec())