import PyQt4
from PyQt4.QtGui import *
from PyQt4.QtCore import  *
import sys
import os
import shutil

class picture_viewer(QWidget):
    def __init__(self):
        super(picture_viewer,self).__init__()

        self.UI()
        self.layout()
        self.show()
        self.actions()
        self.list_photos = []
        self.current_photo = ""
        self.photo_num = 0
    def UI(self):
        self.menu = QMenuBar() #Create Menu Bar
        self.menu.setMaximumHeight(20)

        #================= Creat Menus

        self.file = self.menu.addMenu("File")

        self.next_photo = QAction("Next Photo",self.file)


        self.pre_photo = QAction("Previews Photo",self.file)

        self.move_photo_ = QAction("Move Photo to destination",self.file)


        self.file.addAction(self.next_photo)

        self.file.addAction(self.pre_photo)

        self.file.addAction(self.move_photo_)

        self.next_photo.setShortcut("right")

        self.pre_photo.setShortcut("left")

        self.move_photo_.setShortcut("Up")


        self.next_photo.triggered.connect(self.nex_photo)

        self.pre_photo.triggered.connect(self.prev_photo)

        self.move_photo_.triggered.connect(self.move_photo)

        #self.chiled_window = QWidget(self)
        self.img_source_path = QLineEdit()
        self.move_icon_sign = QLabel()
        self.move_icon_sign.setMaximumHeight(50)
        self.img_source_path.setReadOnly(True)
        self.img_source_path_lbl = QLabel("Source Path::")
        self.img_source_path_btn = QPushButton("Browse")

        self.img_dist_path = QLineEdit()
        self.img_dist_path.setReadOnly(True)
        self.img_dist_path_lbl = QLabel("Destination Path::")
        self.img_dist_path_btn = QPushButton("Browse")


        self.pic_view = QLabel("Viewer")
        self.pic_view.setMaximumWidth(700)
        self.pic_view.setMaximumHeight(700)
        #self.pic_view.setScaledContents(True)


        self.left_btn = QPushButton("<")
        self.left_btn.clicked.connect(self.prev_photo)
        self.right_btn = QPushButton(">")
        self.right_btn.clicked.connect(self.nex_photo)
        self.photo_name = QLabel()

        self.move_btn = QPushButton("Move to destination")
        self.move_btn.clicked.connect(self.move_photo)


    def layout(self):

        self.main_layout = QVBoxLayout()
        self.menu_layout = QHBoxLayout()
        self.main_layout.addLayout(self.menu_layout)
        self.menu_layout.addWidget(self.menu)
        self.pic_layout = QHBoxLayout()

        self.top_layout02 = QHBoxLayout()

        self.bottom_layout = QHBoxLayout()
        self.bottom_layout02=QHBoxLayout()

        self.top_layout = QHBoxLayout()

        self.top_layout.addWidget(self.img_source_path_lbl)
        self.top_layout.addWidget(self.img_source_path)
        self.top_layout.addWidget(self.img_source_path_btn)

        self.top_layout.addWidget(self.move_icon_sign)

        self.top_layout02.addWidget(self.img_dist_path_lbl)
        self.top_layout02.addWidget(self.img_dist_path)
        self.top_layout02.addWidget(self.img_dist_path_btn)

        # self.pic_layout.addStretch()
        self.pic_layout.addWidget(self.pic_view)
        # self.pic_layout.addWidget(self.move_icon_sign)
        # self.pic_layout.addStretch()

        self.bottom_layout.addWidget(self.left_btn)
        self.bottom_layout.addWidget(self.photo_name)
        self.bottom_layout.addWidget(self.right_btn)

        self.bottom_layout02.addWidget(self.move_btn)

        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.top_layout02)
        self.main_layout.addLayout(self.pic_layout)
        self.main_layout.addLayout(self.bottom_layout)
        self.main_layout.addLayout(self.bottom_layout02)


        self.setLayout(self.main_layout)

    def actions(self):
        self.img_source_path_btn.clicked.connect(self.load_source_img)
        self.img_dist_path_btn.clicked.connect(self.load_dist_img)



    def load_source_img(self):

        shot_path = QFileDialog(self,'Photo Source Folder')
        shot_path.setFileMode(QFileDialog.DirectoryOnly)
        shot_path.setSidebarUrls([QUrl.fromLocalFile("")])
        shot_path.show()
        if shot_path.exec_() == QDialog.Accepted:

            self.list_photos = []

            self.img_source_path.setText(shot_path.selectedFiles()[0] +"/")

            for dirs , root ,photos in os.walk(str(shot_path.selectedFiles()[0] +"/")):


                for photo in photos:

                    if photo.endswith("jpg") or photo.endswith("JPG"):

                        self.list_photos.append(os.path.join(dirs,photo))#str(shot_path.selectedFiles()[0] +"/" +photo))


            self.pic_view.setPixmap(QPixmap(self.list_photos[0]).scaled(self.pic_view.width(),self.pic_view.height(),Qt.KeepAspectRatio))
            self.move_icon_sign.setPixmap(QPixmap("icons/green.png").scaled(50,50,Qt.KeepAspectRatio))

    def load_dist_img(self):

        shot_path = QFileDialog(self,'Photo Destination Folder')
        shot_path.setFileMode(QFileDialog.DirectoryOnly)
        shot_path.setSidebarUrls([QUrl.fromLocalFile("")])
        shot_path.show()
        if shot_path.exec_() == QDialog.Accepted:

            self.img_dist_path.setText(shot_path.selectedFiles()[0] +"/")

    def nex_photo(self):
        if len(self.list_photos) > 0:
            self.move_icon_sign.setPixmap(QPixmap("icons/green.png").scaled(50,50,Qt.KeepAspectRatio))
            self.photo_num += 1
            self.pic_view.setPixmap(QPixmap(self.list_photos[self.photo_num]).scaled(self.pic_view.width(),self.pic_view.height(),Qt.KeepAspectRatio))
            self.photo_name.setText(os.path.basename(self.list_photos[self.photo_num]))
            self.photo_name.setStyleSheet("color:black;")
    def prev_photo(self):
        if len(self.list_photos) > 0:
            self.move_icon_sign.setPixmap(QPixmap("icons/green.png").scaled(50,50,Qt.KeepAspectRatio))
            self.photo_num -= 1
            self.pic_view.setPixmap(QPixmap(self.list_photos[self.photo_num]).scaled(self.pic_view.width(),self.pic_view.height(),Qt.KeepAspectRatio))
            self.photo_name.setText(os.path.basename(self.list_photos[self.photo_num]))
            self.photo_name.setStyleSheet("color:black;")

    def move_photo(self):
        if self.img_dist_path.text() != "" and self.img_source_path.text() != "" :
            self.move_icon_sign.setPixmap(QPixmap("icons/red.png").scaled(50,50,Qt.KeepAspectRatio))
            shutil.move( str(self.list_photos[self.photo_num]),str(self.img_dist_path.text() + os.path.basename(self.list_photos[self.photo_num])) )
            self.photo_name.setStyleSheet("color:red;")
        else:
            QMessageBox.warning(self,"Warning","Set Valid Destination Path , Please !")


class main_picture_viewer(QMainWindow):
    def __init__(self):
        super(main_picture_viewer,self).__init__()
        self.setWindowTitle("Picture Separater 1.0")
        self.UI()
        self.layout()
        self.show()

    def UI(self):
        self.pic_viewer = picture_viewer()

        self.setCentralWidget(self.pic_viewer)
    def layout(self):
        pass





def main():
    app =  QApplication(sys.argv)


    ui = main_picture_viewer()

    sys.exit(app.exec_())


if __name__ == "__main__":

    main()
