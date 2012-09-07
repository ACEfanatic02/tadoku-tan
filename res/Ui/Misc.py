#!/usr/bin/python -uOO
# -*- coding: utf-8 -*-

######
##  Tadoku-Tan -- Offline Tadoku Reading Log
##  Misc.py -- Miscellaneous ui dialogs.
######

import logging
import sys

sys.path.append(".")
from tadokutan import Config_new as Config

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_TweetDlg(object):

    def setupUi(self, TweetDlg):
        # Dialog setup:
        TweetDlg.resize(350, 27)
        TweetDlg.setWindowTitle(_fromUtf8("Generated Tweet:"))

        # Text box to hold the tweet:
        self.tweetBox = QtGui.QLineEdit(parent = TweetDlg)
        self.tweetBox.setReadOnly(True)
        self.tweetBox.setMinimumWidth(350)

class TweetDlg(QtGui.QDialog):

    def __init__(self, tweet):
        QtGui.QDialog.__init__(self)

        # Validation
        if not isinstance(tweet, str):
            logging.error("Tweet Dialog Error: received invalid, non-string tweet.")
            raise TypeError

        self.ui = Ui_TweetDlg()
        self.ui.setupUi(self)
        self.ui.tweetBox.setText(_fromUtf8(tweet))
        self.show()


class Ui_ConfigDlg(object):

    def setupUi(self, ConfigDlg):
        # Dialog setup:
        ConfigDlg.resize(350, 250) ## TODO: Adjust size as necessary
        ConfigDlg.setWindowTitle(_fromUtf8("Configuration Settings"))
        ConfigDlg.setModal(True)

        # Input:
        self.twitterlb  = QtGui.QLabel(_fromUtf8("Twitter:"))
        self.twitterButtons = QtGui.QButtonGroup()
        self.twitterButtons.setExclusive(True)
        self.twitterOn  = QtGui.QRadioButton(_fromUtf8("On"), parent=ConfigDlg)
        self.twitterOff = QtGui.QRadioButton(_fromUtf8("Off"), parent=ConfigDlg)

        self.bookVal    = QtGui.QLineEdit()
        self.bookDrVal  = QtGui.QLineEdit()
        self.mangaVal   = QtGui.QLineEdit()
        self.lyricVal   = QtGui.QLineEdit()
        self.webVal     = QtGui.QLineEdit()
        self.newsVal    = QtGui.QLineEdit()
        self.flgameVal  = QtGui.QLineEdit()
        self.gameVal    = QtGui.QLineEdit()
        self.nicoVal    = QtGui.QLineEdit()
        self.subsVal    = QtGui.QLineEdit()
        self.sentVal    = QtGui.QLineEdit()

        # Input validation:
        self.dblValidator = QtGui.QDoubleValidator()
        self.bookVal.setValidator(self.dblValidator)
        self.bookDrVal.setValidator(self.dblValidator)
        self.mangaVal.setValidator(self.dblValidator)
        self.lyricVal.setValidator(self.dblValidator)
        self.webVal.setValidator(self.dblValidator)
        self.newsVal.setValidator(self.dblValidator)
        self.flgameVal.setValidator(self.dblValidator)
        self.gameVal.setValidator(self.dblValidator)
        self.nicoVal.setValidator(self.dblValidator)
        self.subsVal.setValidator(self.dblValidator)
        self.sentVal.setValidator(self.dblValidator)

        # Labels:
        self.booklb     = QtGui.QLabel(_fromUtf8("Book:"))
        self.bookDrlb   = QtGui.QLabel(_fromUtf8("Book (DR):"))
        self.mangalb    = QtGui.QLabel(_fromUtf8("Manga:"))
        self.lyriclb    = QtGui.QLabel(_fromUtf8("Lyrics:"))
        self.weblb      = QtGui.QLabel(_fromUtf8("Net:"))
        self.newslb     = QtGui.QLabel(_fromUtf8("News:"))
        self.flgamelb   = QtGui.QLabel(_fromUtf8("Full Game:"))
        self.gamelb     = QtGui.QLabel(_fromUtf8("Game:"))
        self.nicolb     = QtGui.QLabel(_fromUtf8("Nico:"))
        self.subslb     = QtGui.QLabel(_fromUtf8("Subtitles:"))
        self.sentlb     = QtGui.QLabel(_fromUtf8("Sentences:"))

        # Buttons:
        self.buttonBox = QtGui.QDialogButtonBox(ConfigDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ConfigDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ConfigDlg.reject)
        self.buttonBox.setFocus()

        self.setupLayout(ConfigDlg)

    def setupLayout(self, ConfigDlg):
        self.cfgTableLayout = QtGui.QGridLayout(ConfigDlg)

        # Labels:
        self.cfgTableLayout.addWidget(self.booklb, 1, 1)
        self.cfgTableLayout.addWidget(self.bookDrlb, 2, 1)
        self.cfgTableLayout.addWidget(self.mangalb, 3, 1)
        self.cfgTableLayout.addWidget(self.lyriclb, 4, 1)
        self.cfgTableLayout.addWidget(self.weblb, 5, 1)
        self.cfgTableLayout.addWidget(self.newslb, 6, 1)
        self.cfgTableLayout.addWidget(self.flgamelb, 7, 1)
        self.cfgTableLayout.addWidget(self.gamelb, 8, 1)
        self.cfgTableLayout.addWidget(self.nicolb, 9, 1)
        self.cfgTableLayout.addWidget(self.subslb, 10, 1)
        self.cfgTableLayout.addWidget(self.sentlb, 11, 1)

        # Inputs
        self.cfgTableLayout.addWidget(self.bookVal, 1, 2)
        self.cfgTableLayout.addWidget(self.bookDrVal, 2, 2)
        self.cfgTableLayout.addWidget(self.mangaVal, 3, 2)
        self.cfgTableLayout.addWidget(self.lyricVal, 4, 2)
        self.cfgTableLayout.addWidget(self.webVal, 5, 2)
        self.cfgTableLayout.addWidget(self.newsVal, 6, 2)
        self.cfgTableLayout.addWidget(self.flgameVal, 7, 2)
        self.cfgTableLayout.addWidget(self.gameVal, 8, 2)
        self.cfgTableLayout.addWidget(self.nicoVal, 9, 2)
        self.cfgTableLayout.addWidget(self.subsVal, 10, 2)
        self.cfgTableLayout.addWidget(self.sentVal, 11, 2)

        # Radios and buttons:
        self.cfgTableLayout.addWidget(self.twitterlb, 1, 3)
        self.cfgTableLayout.addWidget(self.twitterOn, 2, 3)
        self.cfgTableLayout.addWidget(self.twitterOff, 3, 3)

        self.cfgTableLayout.addWidget(self.buttonBox, 10, 3, 2, 1)

class ConfigDlg(QtGui.QDialog):

    def __init__(self, cfg):
        QtGui.QDialog.__init__(self)

        self.ui = Ui_ConfigDlg()
        self.ui.setupUi(self)

        self.cfg = cfg

        # Set the values of our entry boxes to match our current cfg values:
        self.ui.bookVal.setText(_fromUtf8(str(self.cfg.book)))
        self.ui.bookDrVal.setText(_fromUtf8(str(self.cfg.bookdr)))
        self.ui.mangaVal.setText(_fromUtf8(str(self.cfg.manga)))
        self.ui.lyricVal.setText(_fromUtf8(str(self.cfg.lyric)))
        self.ui.webVal.setText(_fromUtf8(str(self.cfg.web)))
        self.ui.newsVal.setText(_fromUtf8(str(self.cfg.news)))
        self.ui.flgameVal.setText(_fromUtf8(str(self.cfg.fullgame)))
        self.ui.gameVal.setText(_fromUtf8(str(self.cfg.game)))
        self.ui.nicoVal.setText(_fromUtf8(str(self.cfg.nico)))
        self.ui.subsVal.setText(_fromUtf8(str(self.cfg.subs)))
        self.ui.sentVal.setText(_fromUtf8(str(self.cfg.sentences)))

        # Default twitter setting:
        if self.cfg.twitter == True:
            self.ui.twitterOn.setChecked(True)
        else:
            self.ui.twitterOff.setChecked(True)

    def accept(self):
        # Update the config with new values:
        self.cfg.config.set("SCORING", "book", str(self.ui.bookVal.text()))
        self.cfg.config.set("SCORING", "bookdr", str(self.ui.bookDrVal.text()))
        self.cfg.config.set("SCORING", "manga", str(self.ui.mangaVal.text()))
        self.cfg.config.set("SCORING", "lyric", str(self.ui.lyricVal.text()))
        self.cfg.config.set("SCORING", "web", str(self.ui.webVal.text()))
        self.cfg.config.set("SCORING", "news", str(self.ui.newsVal.text()))
        self.cfg.config.set("SCORING", "fullgame", str(self.ui.flgameVal.text()))
        self.cfg.config.set("SCORING", "game", str(self.ui.gameVal.text()))
        self.cfg.config.set("SCORING", "nico", str(self.ui.nicoVal.text()))
        self.cfg.config.set("SCORING", "subs", str(self.ui.subsVal.text()))
        self.cfg.config.set("SCORING", "sentences", str(self.ui.sentVal.text()))

        if self.ui.twitterOn.isChecked():
            self.cfg.config.set("OTHER", "twitter", "True")
        else:
            self.cfg.config.set("OTHER", "twitter", "False")

        QtGui.QDialog.accept(self)

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    dlg = QtGui.QDialog()
    ui = Ui_ConfigDlg()
    ui.setupUi(dlg)
    dlg.show()
    sys.exit(app.exec_())
