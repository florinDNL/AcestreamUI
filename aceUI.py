from PyQt5 import QtCore, QtGui, QtWidgets
import res
import subprocess
    
url = None

class Ui_AceStream(object):

    def setupUi(self, AceStream):
        AceStream.setObjectName("AceStream")
        AceStream.resize(622, 137)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPref/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AceStream.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(AceStream)
        self.centralwidget.setObjectName("centralwidget")
        
        self.inputURL = QtWidgets.QTextEdit(self.centralwidget)
        self.inputURL.setGeometry(QtCore.QRect(70, 20, 541, 31))
        self.inputURL.setObjectName("inputURL")
        self.inputURL.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.inputURL.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.inputURL.setPlaceholderText("Copy the stream link here")
        self.inputURL.textChanged.connect(self.getURL)

        self.labelURL = QtWidgets.QLabel(self.centralwidget)
        self.labelURL.setGeometry(QtCore.QRect(10, 30, 63, 20))
        self.labelURL.setObjectName("labelURL")
        
        
        self.labelPlayer = QtWidgets.QLabel(self.centralwidget)
        self.labelPlayer.setGeometry(QtCore.QRect(10, 70, 63, 20))
        self.labelPlayer.setObjectName("labelPlayer")
        
        self.playerSelect = QtWidgets.QComboBox(self.centralwidget)
        self.playerSelect.setGeometry(QtCore.QRect(70, 60, 81, 34))
        self.playerSelect.setObjectName("playerSelect")
        self.playerSelect.addItem("VLC")
        self.playerSelect.addItem("Totem")
        self.playerSelect.addItem("mplayer")

        
        self.confirmBt = QtWidgets.QPushButton(self.centralwidget)
        self.confirmBt.setGeometry(QtCore.QRect(540, 100, 71, 31))
        self.confirmBt.setObjectName("confirmBt")
        self.confirmBt.clicked.connect(self.stream)

        AceStream.setCentralWidget(self.centralwidget)

        self.retranslateUi(AceStream)
        QtCore.QMetaObject.connectSlotsByName(AceStream)

    def getURL(self):
        global url
        url = self.inputURL.toPlainText()

    def selPlayer(self):
        player = self.playerSelect.currentText()
        return player.lower()

    def stream(self):
        global url
        if url == None:
            self.inputURL.setPlaceholderText("Pleae enter a valid URL!")
        else:
            if 'acestream://' not in url:
                url = 'acestream://'+ url
            command = f"acestream-launcher {url} -p {self.selPlayer()}"
            subprocess.run(command, shell=True)

        
        
    def retranslateUi(self, AceStream):
        _translate = QtCore.QCoreApplication.translate
        AceStream.setWindowTitle(_translate("AceStream", "AceStream"))
        self.labelURL.setText(_translate("AceStream", "URL:"))
        self.labelPlayer.setText(_translate("AceStream", "Player:"))
        self.playerSelect.setItemText(0, _translate("AceStream", "VLC"))
        self.playerSelect.setItemText(1, _translate("AceStream", "mplayer"))
        self.playerSelect.setItemText(2, _translate("AceStream", "totem"))
        self.playerSelect.setItemText(3, _translate("AceStream", "Other"))
        self.confirmBt.setText(_translate("AceStream", "Stream"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AceStream = QtWidgets.QMainWindow()
    ui = Ui_AceStream()
    ui.setupUi(AceStream)
    AceStream.show()
    sys.exit(app.exec_())