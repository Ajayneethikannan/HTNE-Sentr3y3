from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys, webbrowser

from utils.monitor import monitor

from windows.analytics import Analytics
from windows.add_user import AddUser
from windows.auth import Auth

# variable declaration
is_monitor_running = False
REFRESH_TIME = 10


# Main Application
class MainApplication(QtWidgets.QMainWindow):

    # Initialisaton
    def __init__(self):
        super().__init__() # Call the inherited classes __init__ method
        uic.loadUi('./design/main.ui', self) # Load the .ui file

        # Initialising Window
        self.setWindowTitle('Sentr3y3')

        # Child Components
        self.monitorButton = self.findChild(QtWidgets.QPushButton, 'startMonitor')
        self.showAnalyticsButton = self.findChild(QtWidgets.QPushButton, 'showAnalytics')
        self.addUserButton = self.findChild(QtWidgets.QPushButton, 'addUser')
        self.userSettingsButton = self.findChild(QtWidgets.QPushButton, 'userSettings')
        self.currentUserDetails = self.findChild(QtWidgets.QLabel, 'curentUserDetails')
        
        # Event Listners
        self.showAnalyticsButton.clicked.connect(lambda: self.show_window(Analytics, True))
        self.monitorButton.clicked.connect(lambda: self.apply_auth(self.toggle_monitor))
        self.addUserButton.clicked.connect(lambda: self.apply_auth(lambda : self.show_window(AddUser, True)))
        self.userSettingsButton.clicked.connect(lambda: self.apply_auth(lambda: webbrowser.open('http://localhost:8000/admin/details/')))

        # Timer
        self.monitorTimer = QtCore.QTimer(self, interval=1000 * REFRESH_TIME, timeout=lambda: self.monitorProcess(REFRESH_TIME))
        
        # Setting up rogue properties
        self.addUserButton.setStyleSheet("QPushButton {border-image : url(./resources/icons/add-user.svg)};")
        self.userSettingsButton.setStyleSheet("QPushButton {border-image : url(./resources/icons/user.svg)};")

        # Show the GUI
        self.show()


    # Toggle monitor process
    def toggle_monitor(self):
        global is_monitor_running # variable declaration
        is_monitor_running = not is_monitor_running # Toggle Monitor
        monitorButtonText = "Start Monitoring" if not is_monitor_running else "Monitor Running"
        self.monitorButton.setText(monitorButtonText)
        
        if (is_monitor_running):
            self.startMonitorProcess()
        else:
            self.stopMonitorProcess()

    
    # Start Monitoring
    @QtCore.pyqtSlot()
    def startMonitorProcess(self):
        print ("Monitoring Started")
        QtCore.QTimer.singleShot(0, lambda: self.monitorProcess(REFRESH_TIME))
        self.monitorTimer.start()


    # Stop Monitoring
    @QtCore.pyqtSlot()
    def stopMonitorProcess(self):
        print("Monitoring stopped")
        self.monitorTimer.stop()


    # Main monitor process
    def monitorProcess(self, REFRESH_TIME):
        displayText = monitor(REFRESH_TIME) # Get current user information
        self.currentUserDetails.setText(displayText) # Set current user information


    # Authentication Layer
    def apply_auth(self, callback):
        self.auth = Auth()
        self.auth.is_authenticated.connect(callback)
        self.auth.show()

    # Show Window
    def show_window(self, Window, hide):
        self.window = Window()
        self.window.switch_main_signal.connect(self.show)
        self.window.show()

        if (hide):
            self.hide()


app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = MainApplication() # Create an instance of our class
app.exec_() # Start the application


