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
        self.ui = Ui_ConfigDlg()
        self.ui.setupUi(self)

        # oldCfg is given on init; newCfg holds adjusted config values for return on accept
        self.oldCfg = cfg
        self.newCfg = Config.TadokuConfig()
        self.newCfg.createConfig()

        # Set the values of our entry boxes to match our current cfg values:
        self.ui.bookVal.setText(_fromUtf8(self.oldCfg.book))
        self.ui.bookDrVal.setText(_fromUtf8(self.oldCfg.bookdr))
        self.ui.mangaVal.setText(_fromUtf8(self.oldCfg.manga))
        self.ui.lyricVal.setText(_fromUtf8(self.oldCfg.lyric))
        self.ui.webVal.setText(_fromUtf8(self.oldCfg.web))
        self.ui.newsVal.setText(_fromUtf8(self.oldCfg.news))
        self.ui.flgameVal.setText(_fromUtf8(self.oldCfg.fullgame))
        self.ui.gameVal.setText(_fromUtf8(self.oldCfg.game))
        self.ui.nicoVal.setText(_fromUtf8(self.oldCfg.nico))
        self.ui.subsVal.setText(_fromUtf8(self.oldCfg.subs))
        self.ui.sentVal.setText(_fromUtf8(self.oldCfg.sentences))

        # Default twitter setting:
        if self.oldCfg.twitter == True:
            self.ui.twitterOn.setChecked(True)
        else:
            self.ui.twitterOff.setChecked(True)

    def accept(self):
        # Update the config with new values:
        self.newCfg.config.set("SCORING", "book", self.ui.bookVal)
        self.newCfg.config.set("SCORING", "bookdr", self.ui.bookDrVal)
        self.newCfg.config.set("SCORING", "manga", self.ui.mangaVal)
        self.newCfg.config.set("SCORING", "lyric", self.ui.lyricVal)
        self.newCfg.config.set("SCORING", "web", self.ui.webVal)
        self.newCfg.config.set("SCORING", "news", self.ui.newsVal)
        self.newCfg.config.set("SCORING", "fullgame", self.ui.flgameVal)
        self.newCfg.config.set("SCORING", "game", self.ui.gameVal)
        self.newCfg.config.set("SCORING", "nico", self.ui.nicoVal)
        self.newCfg.config.set("SCORING", "subs", self.ui.subsVal)
        self.newCfg.config.set("SCORING", "sentences", self.ui.sentVal)

        if self.ui.twitterOn.isChecked():
            self.newCfg.config.set("OTHER", "twitter", "True")
        else:
            self.newCfg.config.set("OTHER", "twitter", "False")

        self.oldCfg.updateConfig(self.newCfg)
        super.accept(self)

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    dlg = QtGui.QDialog()
    ui = Ui_ConfigDlg()
    ui.setupUi(dlg)
    dlg.show()
    sys.exit(app.exec_())
