import os
import shutil
import subprocess
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QProgressBar, QMessageBox, QLineEdit, QLabel, QDialog, QTextEdit, QHBoxLayout, QFrame, QGridLayout
from PyQt6.QtGui import QPixmap, QFont, QIcon
from PyQt6.QtCore import Qt, QPropertyAnimation, QRect

class AppStore(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MoonStore')
        self.setGeometry(100, 100, 1000, 800)  

        
        self.layout = QVBoxLayout(self)
        self.setStyleSheet('background-image: url("background_image.jpg"); background-size: cover;')

        self.logo_label = QLabel(self)
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont('Arial', 36, QFont.Weight.Bold) 
        self.logo_label.setFont(font)
        self.logo_label.setText('MoonStore')
        self.logo_label.setStyleSheet('color: white;') 
        self.layout.addWidget(self.logo_label)

        
        self.search_layout = QHBoxLayout()
        self.search_box = QLineEdit(self)
        self.search_box.setPlaceholderText('Search')
        self.search_box.setStyleSheet('font-size: 20px; padding: 10px; border: 2px solid #ccc; border-radius: 25px; background-color: rgba(255, 255, 255, 0.9); color: black;')
        self.search_layout.addWidget(self.search_box)

        self.btn_search = QPushButton('Search', self)
        self.btn_search.setStyleSheet('font-size: 20px; padding: 10px 20px; border: 2px solid #007bff; border-radius: 25px; background-color: #007bff; color: white;')
        self.btn_search.clicked.connect(self.searchClicked)
        self.search_layout.addWidget(self.btn_search)

        self.layout.addLayout(self.search_layout)

        
        self.apps_grid_layout = QGridLayout()
        self.apps_grid_layout.setSpacing(20)  

        
        apps_data = self.fetchAppsFromRepository()  

        for i, app_data in enumerate(apps_data):  
            app_icon = QPushButton('', self)
            app_icon.setFixedSize(200, 200)
            app_icon.setIcon(QIcon(app_data['icon']))
            app_icon.setIconSize(app_icon.size())
            app_icon.setStyleSheet('QPushButton { border: 2px solid #ddd; border-radius: 25px; background-color: white; }')
            app_icon.clicked.connect(self.showAppInfo)
            self.apps_grid_layout.addWidget(app_icon, i // 5, i % 5)

        self.layout.addLayout(self.apps_grid_layout)

        self.progress_bar = QProgressBar(self)
        self.layout.addWidget(self.progress_bar)

        self.setLayout(self.layout)

    def fetchAppsFromRepository(self):
        
        apps_data = [
            {'name': 'App 1', 'icon': 'app1_icon.png'},
            {'name': 'App 2', 'icon': 'app2_icon.png'},
            {'name': 'App 3', 'icon': 'app3_icon.png'},
            {'name': 'App 4', 'icon': 'app4_icon.png'},
            {'name': 'App 5', 'icon': 'app5_icon.png'},
            {'name': 'App 6', 'icon': 'app6_icon.png'},
            {'name': 'App 7', 'icon': 'app7_icon.png'},
            {'name': 'App 8', 'icon': 'app8_icon.png'},
            {'name': 'App 9', 'icon': 'app9_icon.png'},
            {'name': 'App 10', 'icon': 'app10_icon.png'},
            # Add more app data as needed
        ]
        return apps_data

    def searchClicked(self):
        search_query = self.search_box.text()
        # Code for searching apps by name

    def downloadArchApp(self, app_name):
        try:
            # pacman 
            subprocess.run(['pacman', '-S', '--noconfirm', app_name])

            QMessageBox.information(self, 'Download Complete', 'App downloaded successfully!')
        except Exception as e:
            QMessageBox.critical(self, 'Download Error', f'Error downloading app:\n{str(e)}')

    def showAppInfo(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('App Information')
        dialog.setFixedSize(600, 400)  

        main_layout = QVBoxLayout()

        
        app_image_label = QLabel(dialog)
        app_image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        app_image_label.setPixmap(QPixmap('app_icon.png'))
        app_image_label.setMaximumSize(150, 150)
        main_layout.addWidget(app_image_label)

        app_name = QLabel('App Name', dialog)
        app_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        app_name.setStyleSheet('font-size: 24px; font-weight: bold; color: black;')
        main_layout.addWidget(app_name)

        
        line = QFrame(dialog)
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        main_layout.addWidget(line)

        
        description_label = QLabel('Description:', dialog)
        description_label.setStyleSheet('font-size: 20px; font-weight: bold; color: black;')
        main_layout.addWidget(description_label)

        description_text = QTextEdit('App description', dialog)
        description_text.setReadOnly(True)
        description_text.setStyleSheet('background-color: rgba(255, 255, 255, 0.9); font-size: 18px; color: black;')
        main_layout.addWidget(description_text)

        
        btn_download = QPushButton('Download', dialog)
        btn_download.setStyleSheet('font-size: 20px; padding: 10px 20px; border: 2px solid #28a745; border-radius: 25px; background-color: #28a745; color: white;')
        btn_download.clicked.connect(lambda: self.downloadArchApp(app_name.text()))
        main_layout.addWidget(btn_download)

        dialog.setLayout(main_layout)

        
        dialog_animation = QPropertyAnimation(dialog, b"geometry")
        dialog_animation.setDuration(300)
        dialog_animation.setStartValue(QRect(0, 0, 0, 0))
        dialog_animation.setEndValue(QRect(0, 0, 600, 400))
        dialog_animation.start()

        dialog.exec()

if __name__ == '__main__':
    app = QApplication([])
    store = AppStore()
    store.show()
    app.exec()
