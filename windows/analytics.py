from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys, time

from utils.userDetailsText import getUsers, currentUserDetails


# analytics application
class Analytics(QtWidgets.QMainWindow):

    # Switch Main Signal
    switch_main_signal = QtCore.pyqtSignal()

    # Initialisaton
    def __init__(self):
        super().__init__() # Call the inherited classes __init__ method
        uic.loadUi('./design/analytics.ui', self) # Load the .ui file

        # Initialising variables
        self.apps = []
        self.users = []

        # Initialising Window
        self.setWindowTitle('Sentr3y3 - Analytics')

        # Child Components
        self.userDropDown = self.findChild(QtWidgets.QComboBox, 'userDropDown')
        self.appDropDown = self.findChild(QtWidgets.QComboBox, 'appDropDown')
        self.homeButton = self.findChild(QtWidgets.QPushButton, 'home')
        self.displayTable  = self.findChild(QtWidgets.QTableWidget, 'displayTable')

        # Initialising Table
        self.displayTable.setHorizontalHeaderLabels(["Property", "Value (secs)"])
        header = self.displayTable.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

        # Event Listners
        self.homeButton.clicked.connect(self.switch_main)
        self.userDropDown.currentTextChanged.connect(self.update_apps)
        self.appDropDown.currentTextChanged.connect(self.display_statistics)

        # Analytics timer
        self.analyticsTimer = QtCore.QTimer(self, interval=1000 * 10, timeout=self.update)

        # Start the update process
        self.start_update_process()

    
    # Start Updating
    @QtCore.pyqtSlot()
    def start_update_process(self):
        QtCore.QTimer.singleShot(0, self.update)
        self.analyticsTimer.start()


    # Stop Updating
    @QtCore.pyqtSlot()
    def stop_update_process(self):
        self.analyticsTimer.stop()


    # Get apps for selected user
    def update_apps(self):

        # variable declaration
        users = self.users
        apps = self.apps

        # fetching apps for the user
        username = str(self.userDropDown.currentText())
        username, user_id = users[[user[0] for user in users].index(username)]
        self.apps = currentUserDetails(user_id)[2]
        
        # updating applist if needed
        if (self.apps != apps):
            appTitles = [app['title'] for app in self.apps]
            self.appDropDown.clear()
            self.appDropDown.addItems(appTitles)


    # Display selected app statistics
    def display_statistics(self):

        # variable declaration
        apps = self.apps

        # get selected app
        selected_app = str(self.appDropDown.currentText())

        # display stats
        for app in apps:
            
            if (app['title'] == selected_app):
                
                # display usage time
                item = QtWidgets.QTableWidgetItem()
                item.setText(str(app['time_today']))
                self.displayTable.setItem(0, 1, item)

                # display time limit
                item = QtWidgets.QTableWidgetItem()
                item.setText(str(app['time_limit']))
                self.displayTable.setItem(1, 1, item)

                # display remaining time
                item = QtWidgets.QTableWidgetItem()
                item.setText(str(app['time_limit'] - app['time_today']))
                self.displayTable.setItem(2, 1, item)


    # update process
    def update(self):

        # print run analytics
        print("analytics running")
        
        # variable declaration
        users = self

        # fetching users
        self.users = getUsers()

        # update user data
        if (len(self.users) > 0):
            if (self.users != users):
                print("here")
                self.userDropDown.clear()
                self.userDropDown.addItems([user[0] for user in self.users])

            # update apps
            self.update_apps()

            # display stats
            self.display_statistics()


    # Switch back to main window
    def switch_main(self):

        # stop update process
        self.stop_update_process()

        # switch to main application
        self.switch_main_signal.emit()
        self.close()





