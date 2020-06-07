from PyQt5 import QtCore, QtGui, QtWidgets, uic


# Authentication Window
class Auth(QtWidgets.QMainWindow):

    # Switch Window Signal
    is_authenticated = QtCore.pyqtSignal()

    # Initialisaton
    def __init__(self):
        super().__init__() # Call the inherited classes __init__ method
        uic.loadUi('./design/authentication.ui', self) # Load the .ui file

        # Components
        self.submit = self.findChild(QtWidgets.QPushButton, 'submit')
        self.password = self.findChild(QtWidgets.QLineEdit, 'password')
        self.back = self.findChild(QtWidgets.QPushButton, 'back')

        # Event Listners
        self.submit.clicked.connect(self.authenticate)
        self.back.clicked.connect(self.close)

    # Authenticate
    def authenticate(self):
        if self.password.text() == 'helloiitr': # hardcoded. Just showing proof of concept
            self.is_authenticated.emit()

        self.password.clear()
        self.close()