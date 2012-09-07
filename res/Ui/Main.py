#!/usr/bin/python -uOO
# -*- coding: utf-8 -*-

######
##  Tadoku-Tan -- Offline Tadoku Reading Log
##  Main.py -- ui for main window
######

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        # Setup the window itself and its central widget
        MainWindow.setFixedSize(400, 300)
        MainWindow.setWindowTitle("Tadoku-Tan")
        self.centralwidget = QtGui.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        # Setup individual parts of the window
        self.setupMediaButtons(MainWindow)
        self.setupMenuAndStatusBars(MainWindow)
        self.setupSubmitAndLabels(MainWindow)

        # Setup the overall layout of the window
        self.setupLayout()

    def setupMediaButtons(self, MainWindow):
        # Setup group box surrounding the media selections
        self.mediaBox = QtGui.QGroupBox(self.centralwidget)
        self.mediaBox.setGeometry(QtCore.QRect(225, 0, 200, 250))
        self.mediaBox.setTitle("Media:")
        self.mediaButtonGroup = QtGui.QButtonGroup(self.mediaBox)

        # Create media radio buttons and checkboxes
        self.book_radio   = QtGui.QRadioButton(_fromUtf8("Book"), parent=self.mediaBox)
        self.manga_radio  = QtGui.QRadioButton(_fromUtf8("Manga"), parent=self.mediaBox)
        self.flgame_radio = QtGui.QRadioButton(_fromUtf8("Full Game"), parent=self.mediaBox)
        self.game_radio   = QtGui.QRadioButton(_fromUtf8("Game"), parent=self.mediaBox)
        self.net_radio    = QtGui.QRadioButton(_fromUtf8("Net"), parent=self.mediaBox)
        self.news_radio   = QtGui.QRadioButton(_fromUtf8("News"), parent=self.mediaBox)
        self.nico_radio   = QtGui.QRadioButton(_fromUtf8("Nico"), parent=self.mediaBox)
        self.subs_radio   = QtGui.QRadioButton(_fromUtf8("Subtitles"), parent=self.mediaBox)
        self.sent_radio   = QtGui.QRadioButton(_fromUtf8("Sentences"), parent=self.mediaBox)
        self.lyric_radio  = QtGui.QRadioButton(_fromUtf8("Lyrics"), parent=self.mediaBox)
        self.dr_check     = QtGui.QCheckBox(_fromUtf8("Double-rowed"), parent=self.mediaBox)

        # Link radio buttons to button group
        self.mediaButtonGroup.addButton(self.book_radio)
        self.mediaButtonGroup.addButton(self.manga_radio)
        self.mediaButtonGroup.addButton(self.flgame_radio)
        self.mediaButtonGroup.addButton(self.game_radio)
        self.mediaButtonGroup.addButton(self.net_radio)
        self.mediaButtonGroup.addButton(self.news_radio)
        self.mediaButtonGroup.addButton(self.nico_radio)
        self.mediaButtonGroup.addButton(self.subs_radio)
        self.mediaButtonGroup.addButton(self.sent_radio)
        self.mediaButtonGroup.addButton(self.lyric_radio)

        # Some misc setup
        self.mediaButtonGroup.setExclusive(True)
        self.book_radio.setChecked(True)
        self.book_radio.toggled.connect(self._drTie)

        # Setup sub-layout for the media buttons
        self.mediaGrid = QtGui.QVBoxLayout()
        self.mediaGrid.setGeometry(QtCore.QRect(225, 0, 200, 250))
        self.mediaGrid.addWidget(self.book_radio)
        self.mediaGrid.addWidget(self.manga_radio)
        self.mediaGrid.addWidget(self.flgame_radio)
        self.mediaGrid.addWidget(self.game_radio)
        self.mediaGrid.addWidget(self.news_radio)
        self.mediaGrid.addWidget(self.nico_radio)
        self.mediaGrid.addWidget(self.subs_radio)
        self.mediaGrid.addWidget(self.sent_radio)
        self.mediaGrid.addWidget(self.lyric_radio)
        self.mediaGrid.addWidget(self.net_radio)
        self.mediaGrid.addWidget(self.dr_check)
        self.mediaGrid.addStretch(1)
        self.mediaBox.setLayout(self.mediaGrid)

    def setupMenuAndStatusBars(self, MainWindow):
        # Status bar
        self.statusbar = QtGui.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        # Menu bar
        self.menubar = QtGui.QMenuBar(MainWindow)
        MainWindow.setMenuBar(self.menubar)

        # File menu
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setTitle(_fromUtf8("&File"))
        self.actionLoad = QtGui.QAction(MainWindow)
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionLoad.setText(_fromUtf8("&Load..."))
        self.actionSave.setText(_fromUtf8("&Save"))
        self.actionExit.setText(_fromUtf8("E&xit"))

        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)

        # Tools menu
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setTitle(_fromUtf8("&Tools"))
        self.actionConfig = QtGui.QAction(MainWindow)
        self.actionConfig.setText(_fromUtf8("&Config Settings..."))

        self.menuTools.addAction(self.actionConfig)

        self.menubar.addMenu(self.menuFile)
        self.menubar.addMenu(self.menuTools)

    def setupSubmitAndLabels(self, MainWindow):
        # Create submit fields
        self.amountRead = QtGui.QLineEdit(self.centralwidget)
        self.timesRead  = QtGui.QLineEdit(self.centralwidget)

        # Buttons
        self.submitButton  = QtGui.QPushButton(self.centralwidget)
        self.scoresButton  = QtGui.QPushButton(self.centralwidget)
        self.entriesButton = QtGui.QPushButton(self.centralwidget)
        self.submitButton.setText(_fromUtf8("Submit"))
        self.scoresButton.setText(_fromUtf8("Scores..."))
        self.entriesButton.setText(_fromUtf8("Entries..."))

        # Score labels
        self.totalscorelb = QtGui.QLabel(_fromUtf8("Total Score:"), parent=self.centralwidget)
        self.total_score  = QtGui.QLabel(_fromUtf8("0"), parent=self.centralwidget)
        self.total_score.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)

        # Setup sub-layout for submit fields
        self.submitLayout = QtGui.QGridLayout()
        self.submitLayout.setVerticalSpacing(10)
        self.submitLayout.addWidget(QtGui.QLabel(_fromUtf8("Amount Read:")),
                                    1, 1)
        self.submitLayout.addWidget(QtGui.QLabel(_fromUtf8("Times Read:")),
                                    2, 1)
        self.submitLayout.addWidget(self.amountRead, 1, 2, 1, 2)
        self.submitLayout.addWidget(self.timesRead, 2, 2, 1, 2)
        self.submitLayout.addWidget(self.submitButton, 3, 1,)

        self.submitLayout.addWidget(self.totalscorelb, 5, 1, 1, 1)
        self.submitLayout.addWidget(self.total_score, 5, 2, 1, 2)

        self.submitLayout.addWidget(self.scoresButton, 6, 1)
        self.submitLayout.addWidget(self.entriesButton, 6, 2)

        self.top_spacer    = QtGui.QSpacerItem(200, 15)
        self.bottom_spacer = QtGui.QSpacerItem(200, 20)
        self.mid_spacer    = QtGui.QSpacerItem(200, 40)
        self.left_spacer   = QtGui.QSpacerItem(10, 200)
        self.submitLayout.addItem(self.top_spacer, 0, 1, 1, 3)
        self.submitLayout.addItem(self.mid_spacer, 4, 1, 1, 3)
        self.submitLayout.addItem(self.bottom_spacer, 7, 1, 1, 3)
        self.submitLayout.addItem(self.left_spacer, 1, 0, 7, 1)

    def setupLayout(self):
        self.mainLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.mainLayout.addLayout(self.submitLayout)
        self.mainLayout.addWidget(self.mediaBox)

    def _drTie(self):
        if self.book_radio.isChecked():
            self.dr_check.setEnabled(True)
        else:
            self.dr_check.setEnabled(False)



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

