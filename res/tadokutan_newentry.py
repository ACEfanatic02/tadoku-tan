# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Bryan Taylor/Documents/ui/tadokutan_newentry.ui'
#
# Created: Sat Jun 02 13:43:50 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	_fromUtf8 = lambda s: s

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.resize(310, 249)
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.mediaBox = QtGui.QGroupBox(self.centralwidget)
		self.mediaBox.setGeometry(QtCore.QRect(120, 0, 181, 151))
		self.mediaBox.setObjectName(_fromUtf8("mediaBox"))
		self.book_radio = QtGui.QRadioButton(self.mediaBox)
		self.book_radio.setGeometry(QtCore.QRect(10, 20, 82, 17))
		self.book_radio.setObjectName(_fromUtf8("book_radio"))
		self.mediaButtonGroup = QtGui.QButtonGroup(MainWindow)
		self.mediaButtonGroup.setObjectName(_fromUtf8("mediaButtonGroup"))
		self.mediaButtonGroup.addButton(self.book_radio)
		self.manga_radio = QtGui.QRadioButton(self.mediaBox)
		self.manga_radio.setGeometry(QtCore.QRect(10, 40, 82, 17))
		self.manga_radio.setObjectName(_fromUtf8("manga_radio"))
		self.mediaButtonGroup.addButton(self.manga_radio)
		self.flgame_radio = QtGui.QRadioButton(self.mediaBox)
		self.flgame_radio.setGeometry(QtCore.QRect(10, 60, 82, 17))
		self.flgame_radio.setObjectName(_fromUtf8("flgame_radio"))
		self.mediaButtonGroup.addButton(self.flgame_radio)
		self.game_radio = QtGui.QRadioButton(self.mediaBox)
		self.game_radio.setGeometry(QtCore.QRect(10, 80, 82, 17))
		self.game_radio.setObjectName(_fromUtf8("game_radio"))
		self.mediaButtonGroup.addButton(self.game_radio)
		self.net_radio = QtGui.QRadioButton(self.mediaBox)
		self.net_radio.setGeometry(QtCore.QRect(10, 100, 82, 17))
		self.net_radio.setObjectName(_fromUtf8("net_radio"))
		self.mediaButtonGroup.addButton(self.net_radio)
		self.news_radio = QtGui.QRadioButton(self.mediaBox)
		self.news_radio.setGeometry(QtCore.QRect(10, 120, 82, 17))
		self.news_radio.setObjectName(_fromUtf8("news_radio"))
		self.mediaButtonGroup.addButton(self.news_radio)
		self.nico_radio = QtGui.QRadioButton(self.mediaBox)
		self.nico_radio.setGeometry(QtCore.QRect(90, 80, 82, 17))
		self.nico_radio.setObjectName(_fromUtf8("nico_radio"))
		self.mediaButtonGroup.addButton(self.nico_radio)
		self.dr_check = QtGui.QCheckBox(self.mediaBox)
		self.dr_check.setGeometry(QtCore.QRect(70, 20, 111, 16))
		self.dr_check.setObjectName(_fromUtf8("dr_check"))
		self.subs_radio = QtGui.QRadioButton(self.mediaBox)
		self.subs_radio.setGeometry(QtCore.QRect(90, 100, 82, 17))
		self.subs_radio.setObjectName(_fromUtf8("subs_radio"))
		self.mediaButtonGroup.addButton(self.subs_radio)
		self.sent_radio = QtGui.QRadioButton(self.mediaBox)
		self.sent_radio.setGeometry(QtCore.QRect(90, 120, 82, 17))
		self.sent_radio.setObjectName(_fromUtf8("sent_radio"))
		self.mediaButtonGroup.addButton(self.sent_radio)
		self.lyric_radio = QtGui.QRadioButton(self.mediaBox)
		self.lyric_radio.setGeometry(QtCore.QRect(90, 60, 82, 17))
		self.lyric_radio.setObjectName(_fromUtf8("lyric_radio"))
		self.mediaButtonGroup.addButton(self.lyric_radio)
		self.amountRead = QtGui.QLineEdit(self.centralwidget)
		self.amountRead.setGeometry(QtCore.QRect(12, 30, 101, 20))
		self.amountRead.setObjectName(_fromUtf8("amountRead"))
		self.amountlb = QtGui.QLabel(self.centralwidget)
		self.amountlb.setGeometry(QtCore.QRect(10, 10, 101, 16))
		self.amountlb.setObjectName(_fromUtf8("amountlb"))
		self.submitButton = QtGui.QPushButton(self.centralwidget)
		self.submitButton.setGeometry(QtCore.QRect(20, 120, 75, 23))
		self.submitButton.setAutoDefault(True)
		self.submitButton.setObjectName(_fromUtf8("submitButton"))
		self.scoresButton = QtGui.QPushButton(self.centralwidget)
		self.scoresButton.setGeometry(QtCore.QRect(20, 180, 75, 23))
		self.scoresButton.setObjectName(_fromUtf8("scoresButton"))
		self.entriesButton = QtGui.QPushButton(self.centralwidget)
		self.entriesButton.setGeometry(QtCore.QRect(20, 150, 75, 23))
		self.entriesButton.setObjectName(_fromUtf8("entriesButton"))
		self.timelb = QtGui.QLabel(self.centralwidget)
		self.timelb.setGeometry(QtCore.QRect(10, 60, 101, 16))
		self.timelb.setObjectName(_fromUtf8("timelb"))
		self.timesRead = QtGui.QLineEdit(self.centralwidget)
		self.timesRead.setGeometry(QtCore.QRect(10, 80, 101, 20))
		self.timesRead.setObjectName(_fromUtf8("timesRead"))
		self.totalscorelb = QtGui.QLabel(self.centralwidget)
		self.totalscorelb.setGeometry(QtCore.QRect(120, 160, 181, 16))
		self.totalscorelb.setObjectName(_fromUtf8("totalscorelb"))
		self.total_score = QtGui.QLabel(self.centralwidget)
		self.total_score.setGeometry(QtCore.QRect(180, 160, 111, 16))
		self.total_score.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.total_score.setObjectName(_fromUtf8("total_score"))
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 310, 21))
		self.menubar.setObjectName(_fromUtf8("menubar"))
		self.menuFile = QtGui.QMenu(self.menubar)
		self.menuFile.setObjectName(_fromUtf8("menuFile"))
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtGui.QStatusBar(MainWindow)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		MainWindow.setStatusBar(self.statusbar)
		self.actionLoad = QtGui.QAction(MainWindow)
		self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
		self.actionSave = QtGui.QAction(MainWindow)
		self.actionSave.setObjectName(_fromUtf8("actionSave"))
		self.actionExit = QtGui.QAction(MainWindow)
		self.actionExit.setObjectName(_fromUtf8("actionExit"))
		self.menuFile.addAction(self.actionLoad)
		self.menuFile.addAction(self.actionSave)
		self.menuFile.addSeparator()
		self.menuFile.addAction(self.actionExit)
		self.menubar.addAction(self.menuFile.menuAction())

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Tadoku-Tan", None, QtGui.QApplication.UnicodeUTF8))
		self.mediaBox.setTitle(QtGui.QApplication.translate("MainWindow", "Media:", None, QtGui.QApplication.UnicodeUTF8))
		self.book_radio.setText(QtGui.QApplication.translate("MainWindow", "Book", None, QtGui.QApplication.UnicodeUTF8))
		self.manga_radio.setText(QtGui.QApplication.translate("MainWindow", "Manga", None, QtGui.QApplication.UnicodeUTF8))
		self.flgame_radio.setText(QtGui.QApplication.translate("MainWindow", "Full Game", None, QtGui.QApplication.UnicodeUTF8))
		self.game_radio.setText(QtGui.QApplication.translate("MainWindow", "Game", None, QtGui.QApplication.UnicodeUTF8))
		self.net_radio.setText(QtGui.QApplication.translate("MainWindow", "Net", None, QtGui.QApplication.UnicodeUTF8))
		self.news_radio.setText(QtGui.QApplication.translate("MainWindow", "News", None, QtGui.QApplication.UnicodeUTF8))
		self.nico_radio.setText(QtGui.QApplication.translate("MainWindow", "NicoNico", None, QtGui.QApplication.UnicodeUTF8))
		self.dr_check.setText(QtGui.QApplication.translate("MainWindow", "Double-Rowed", None, QtGui.QApplication.UnicodeUTF8))
		self.subs_radio.setText(QtGui.QApplication.translate("MainWindow", "Subtitles", None, QtGui.QApplication.UnicodeUTF8))
		self.sent_radio.setText(QtGui.QApplication.translate("MainWindow", "Sentences", None, QtGui.QApplication.UnicodeUTF8))
		self.lyric_radio.setText(QtGui.QApplication.translate("MainWindow", "Lyrics", None, QtGui.QApplication.UnicodeUTF8))
		self.amountlb.setText(QtGui.QApplication.translate("MainWindow", "Amount Read:", None, QtGui.QApplication.UnicodeUTF8))
		self.submitButton.setText(QtGui.QApplication.translate("MainWindow", "Submit", None, QtGui.QApplication.UnicodeUTF8))
		self.scoresButton.setText(QtGui.QApplication.translate("MainWindow", "Scores...", None, QtGui.QApplication.UnicodeUTF8))
		self.entriesButton.setText(QtGui.QApplication.translate("MainWindow", "Entries...", None, QtGui.QApplication.UnicodeUTF8))
		self.timelb.setText(QtGui.QApplication.translate("MainWindow", "Times Read:", None, QtGui.QApplication.UnicodeUTF8))
		self.timesRead.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Leave blank for 1st", None, QtGui.QApplication.UnicodeUTF8))
		self.totalscorelb.setText(QtGui.QApplication.translate("MainWindow", "Total Score:", None, QtGui.QApplication.UnicodeUTF8))
		self.total_score.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
		self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
		self.actionLoad.setText(QtGui.QApplication.translate("MainWindow", "&Load...", None, QtGui.QApplication.UnicodeUTF8))
		self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
		self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "E&xit", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	MainWindow = QtGui.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())

