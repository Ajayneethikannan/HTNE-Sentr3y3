from PyQt5 import QtCore, QtGui, QtWidgets, uic
import pickle, requests, json, os

from utils.add_face import add_face

# main application
class AddUser(QtWidgets.QMainWindow):

    # Switch Main Signal
    switch_main_signal = QtCore.pyqtSignal()

    # Initialisation
    def __init__(self):
        super().__init__() # Call the inherited classes __init__ method
        uic.loadUi('./design/add_user.ui', self) # Load the .ui file

        # Initialising Window
        self.setWindowTitle('Sentr3y3 - Add User')

        # Child Components
        self.photoButton = self.findChild(QtWidgets.QPushButton, 'photo')
        self.nameField = self.findChild(QtWidgets.QTextEdit, 'name')
        self.underAgeButton = self.findChild(QtWidgets.QCheckBox, 'underAge')
        self.homeButton = self.findChild(QtWidgets.QPushButton, 'home')

        # events
        self.homeButton.clicked.connect(self.switch_main)
        self.photoButton.clicked.connect(self.add_photo)


    # add photo
    def add_photo(self):
        encoding = add_face()
        if not os.path.exists("./userData"):
            os.makedirs(("./userData"))

        with open("./userData/faces_encodings.txt", "wb+") as fp:
            try:
                known_face_encodings = pickle.load(fp)
            except EOFError:
                known_face_encodings = []

        with open("./userData/ids.txt", "wb+") as fp:
            try:
                known_face_ids =  pickle.load(fp)
            except EOFError:
                known_face_ids = []

        obj = {
            "is_underage": self.underAgeButton.isChecked(),
            "is_admin": False,
            "username": self.nameField.toPlainText()
        }

        print(obj, ' added successfully')
        r = requests.post('http://localhost:8000/users/', json=obj)
        print(r.content)
        id = int(json.loads(r.content)["id"])
        known_face_ids.append(id)
        known_face_encodings.append(encoding)
        print(known_face_ids)

        with open("./userData/faces_encodings.txt", "wb") as fp:
            pickle.dump(known_face_encodings, fp)

        with open("./userData/ids.txt", "wb") as fp:
            pickle.dump(known_face_ids, fp)

        # switch back to main window after completion
        self.switch_main()


    # Switch back to main window
    def switch_main(self):
        self.switch_main_signal.emit()
        self.close()