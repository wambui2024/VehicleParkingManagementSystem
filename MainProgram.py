import sys
import os
from InstallWindow import InstallWindow
from LoginWindow import LoginScreen
from PyQt5.QtWidgets import QApplication,QSplashScreen,QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt,QTimer
class MainScreen():
    def showSplashScreen(self):
        self.pix=QPixmap("slash_img.jpg")
        self.splassh=QSplashScreen(self.pix,Qt.WindowStaysOnTopHint)
        self.splassh.show()

def showSetupWindow():
    mainScreen.splassh.close()
    installWindow.show()

def showLoginWindow():
    mainScreen.splassh.close()
    login.showLoginScreen()


#initialize the QApplication object which is necessary for managing application settingsand the event loop
app=QApplication(sys.argv)
#creates an instance of the loginscreen class which represents the login window of the application
login=LoginScreen()
mainScreen=MainScreen()
mainScreen.showSplashScreen()
installWindow=InstallWindow()

if os.path.exists("./config.json"):
    QTimer.singleShot(3000,showLoginWindow)
else:
    QTimer.singleShot(3000,showSetupWindow)


sys.exit(app.exec_())