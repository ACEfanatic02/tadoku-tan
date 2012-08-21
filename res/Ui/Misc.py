#!/usr/bin/python -uOO
# -*- coding: utf-8 -*-

######
##  Tadoku-Tan -- Offline Tadoku Reading Log
##  Misc.py -- Miscellaneous ui dialogs.
######

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


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    dlg = TweetDlg("@TadokuBot: This is a test! Nothing more...")
    sys.exit(app.exec_())