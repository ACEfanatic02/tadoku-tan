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
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setFixedSize(400, 300)
        MainWindow.setWindowTitle("Tadoku-Tan")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)

        # Setup individual parts of the window
        self.setupMediaButtons()
        self.setupMenuAndStatusBars()
        self.setupSubmitAndLabels()

        # Setup the overall layout of the window
        self.setupLayout()


    def setupMediaButtons(self):
        # Setup group box surrounding the media selections
        self.mediaBox = QtGui.QGroupBox(self.centralwidget)
        self.mediaBox.setGeometry(QtCore.QRect(225, 0, 200, 250))
        self.mediaBox.setObjectName(_fromUtf8("mediaBox"))
        self.mediaBox.setTitle("Media:")
        self.mediaButtonGroup = QtGui.QButtonGroup(self.mediaBox)
        self.mediaButtonGroup.setObjectName(_fromUtf8("self.mediaButtonGroup"))

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

        # Set object names (TODO: CHECK - Is this really necessary?)
        self.book_radio.setObjectName(_fromUtf8("book_radio"))
        self.manga_radio.setObjectName(_fromUtf8("manga_radio"))
        self.flgame_radio.setObjectName(_fromUtf8("flgame_radio"))
        self.game_radio.setObjectName(_fromUtf8("game_radio"))
        self.net_radio.setObjectName(_fromUtf8("net_radio"))
        self.news_radio.setObjectName(_fromUtf8("news_radio"))
        self.nico_radio.setObjectName(_fromUtf8("nico_radio"))
        self.subs_radio.setObjectName(_fromUtf8("subs_radio"))
        self.sent_radio.setObjectName(_fromUtf8("sent_radio"))
        self.lyric_radio.setObjectName(_fromUtf8("lyric_radio"))
        self.dr_check.setObjectName(_fromUtf8("dr_check"))

        # Setup sub-layout for the media buttons
        self.mediaGrid = QtGui.QGridLayout(self.mediaBox)
        self.mediaGrid.addWidget(self.book_radio, 1, 1)
        self.mediaGrid.addWidget(self.manga_radio, 2, 1)
        self.mediaGrid.addWidget(self.flgame_radio, 3, 1)
        self.mediaGrid.addWidget(self.game_radio, 4, 1)
        self.mediaGrid.addWidget(self.news_radio, 5, 1)
        self.mediaGrid.addWidget(self.nico_radio, 6, 1)
        self.mediaGrid.addWidget(self.dr_check, 11, 1,)
        self.mediaGrid.addWidget(self.subs_radio, 7, 1)
        self.mediaGrid.addWidget(self.sent_radio, 8, 1)
        self.mediaGrid.addWidget(self.lyric_radio, 9, 1)
        self.mediaGrid.addWidget(self.net_radio, 10, 1)


    def setupMenuAndStatusBars(self):
        pass

    def setupSubmitAndLabels(self):
        pass

    def setupLayout(self):
        pass

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

