from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QThread
from PyQt5.QtGui import QPixmap
import sys
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    splash_pic = QPixmap('logo.svg')

    splash = QtWidgets.QSplashScreen(splash_pic, Qt.WindowStaysOnTopHint)
    splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
    splash.setEnabled(False)
    splash.setMask(splash_pic.mask())
    splash.showMessage("<h6>Loading...</h6>", Qt.AlignBottom | Qt.AlignRight, Qt.black)
    splash.show()
    app.processEvents()
    app.exec_()