#!/usr/bin/python -uOO
# -*- coding: utf-8 -*-

######
##  Tadoku-Tan -- Offline Tadoku Reading Log
##  Scores.py -- ui for scores dialog
######

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ScoresDlg(object):

    def setupUi(self, ScoresDlg):
        # Set up the dialog itself
        ScoresDlg.resize(400, 280)
        ScoresDlg.setSizeGripEnabled(False)
        ScoresDlg.setWindowTitle(_fromUtf8("Scores"))

        # Buttons
        self.buttonBox = QtGui.QDialogButtonBox(ScoresDlg)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)

        self.scoreValueGroup = QtGui.QButtonGroup(ScoresDlg)
        self.scores_radio    = QtGui.QRadioButton(ScoresDlg)
        self.values_radio    = QtGui.QRadioButton(ScoresDlg)
        self.scores_radio.setText(_fromUtf8("Score"))
        self.values_radio.setText(_fromUtf8("Value"))
        self.scoreValueGroup.addButton(self.scores_radio)
        self.scoreValueGroup.addButton(self.values_radio)
        self.scores_radio.setChecked(True)

        # Total score:
        self.totallb     = QtGui.QLabel(_fromUtf8("Total Score:"), parent=ScoresDlg)
        self.total_score = QtGui.QLabel(_fromUtf8("0"), parent=ScoresDlg)

        self.setupScoretable(ScoresDlg)
        self.setupLayout(ScoresDlg)

    def setupScoretable(self, ScoresDlg):
        # Labels:
        self.booklb   = QtGui.QLabel(_fromUtf8("Book:"), parent=ScoresDlg)
        self.bookdrlb = QtGui.QLabel(_fromUtf8("Book (DR):"), parent=ScoresDlg)
        self.mangalb  = QtGui.QLabel(_fromUtf8("Manga:"), parent=ScoresDlg)
        self.flgamelb = QtGui.QLabel(_fromUtf8("Full Game:"), parent=ScoresDlg)
        self.gamelb   = QtGui.QLabel(_fromUtf8("Game:"), parent=ScoresDlg)
        self.netlb    = QtGui.QLabel(_fromUtf8("Net:"), parent=ScoresDlg)
        self.newslb   = QtGui.QLabel(_fromUtf8("News:"), parent=ScoresDlg)
        self.nicolb   = QtGui.QLabel(_fromUtf8("Nico:"), parent=ScoresDlg)
        self.subslb   = QtGui.QLabel(_fromUtf8("Subtitles:"), parent=ScoresDlg)
        self.sentlb   = QtGui.QLabel(_fromUtf8("Sentences:"), parent=ScoresDlg)
        self.lyriclb  = QtGui.QLabel(_fromUtf8("Lyrics:"), parent=ScoresDlg)

        # Scores:
        self.book_score   = QtGui.QLabel(_fromUtf8("0"), parent=ScoresDlg)
        self.bookdr_score = QtGui.QLabel(_fromUtf8("0"), parent=ScoresDlg)
        self.manga_score  = QtGui.QLabel(_fromUtf8("0"), parent=ScoresDlg)
        self.flgame_score = QtGui.QLabel(_fromUtf8("0"), parent=ScoresDlg)
        self.game_score   = QtGui.QLabel(_fromUtf8("0"), parent=ScoresDlg)
        self.net_score    = QtGui.QLabel(_fromUtf8("0"), parent=ScoresDlg)
        self.news_score   = QtGui.QLabel(_fromUtf8("0"), parent=ScoresDlg)
        self.nico_score   = QtGui.QLabel(_fromUtf8("0"), parent=ScoresDlg)
        self.subs_score   = QtGui.QLabel(_fromUtf8("0"), parent=ScoresDlg)
        self.sent_score   = QtGui.QLabel(_fromUtf8("0"), parent=ScoresDlg)
        self.lyric_score  = QtGui.QLabel(_fromUtf8("0"), parent=ScoresDlg)

    def setupLayout(self, ScoresDlg):
        # Sublayout for score table:
        self.scoreTableLayout = QtGui.QGridLayout()

        # Labels:
        self.scoreTableLayout.addWidget(self.booklb, 1, 1)
        self.scoreTableLayout.addWidget(self.bookdrlb, 2, 1)
        self.scoreTableLayout.addWidget(self.mangalb, 3, 1)
        self.scoreTableLayout.addWidget(self.flgamelb, 4, 1)
        self.scoreTableLayout.addWidget(self.gamelb, 5, 1)
        self.scoreTableLayout.addWidget(self.netlb, 6, 1)
        self.scoreTableLayout.addWidget(self.newslb, 7, 1)
        self.scoreTableLayout.addWidget(self.nicolb, 8, 1)
        self.scoreTableLayout.addWidget(self.subslb, 9, 1)
        self.scoreTableLayout.addWidget(self.sentlb, 10, 1)
        self.scoreTableLayout.addWidget(self.lyriclb, 11, 1)
        self.scoreTableLayout.addWidget(self.totallb, 12, 1)

        # Scores:
        self.scoreTableLayout.addWidget(self.book_score, 1, 2, alignment=QtCore.Qt.AlignRight)
        self.scoreTableLayout.addWidget(self.bookdr_score, 2, 2, alignment=QtCore.Qt.AlignRight)
        self.scoreTableLayout.addWidget(self.manga_score, 3, 2, alignment=QtCore.Qt.AlignRight)
        self.scoreTableLayout.addWidget(self.flgame_score, 4, 2, alignment=QtCore.Qt.AlignRight)
        self.scoreTableLayout.addWidget(self.game_score, 5, 2, alignment=QtCore.Qt.AlignRight)
        self.scoreTableLayout.addWidget(self.net_score, 6, 2, alignment=QtCore.Qt.AlignRight)
        self.scoreTableLayout.addWidget(self.news_score, 7, 2, alignment=QtCore.Qt.AlignRight)
        self.scoreTableLayout.addWidget(self.nico_score, 8, 2, alignment=QtCore.Qt.AlignRight)
        self.scoreTableLayout.addWidget(self.subs_score, 9, 2, alignment=QtCore.Qt.AlignRight)
        self.scoreTableLayout.addWidget(self.sent_score, 10, 2, alignment=QtCore.Qt.AlignRight)
        self.scoreTableLayout.addWidget(self.lyric_score, 11, 2, alignment=QtCore.Qt.AlignRight)
        self.scoreTableLayout.addWidget(self.total_score, 12, 2, alignment=QtCore.Qt.AlignRight)

        # Overall layout:
        self.dialogLayout = QtGui.QGridLayout(ScoresDlg)
        self.dialogLayout.addItem(self.scoreTableLayout, 1, 1, 12, 1)
        self.dialogLayout.addWidget(self.buttonBox, 13, 2)
        self.dialogLayout.addWidget(self.scores_radio, 11, 2)
        self.dialogLayout.addWidget(self.values_radio, 12, 2)

        self.dialogLayout.setColumnStretch(1, 1)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ScoresDlg = QtGui.QDialog()
    ui = Ui_ScoresDlg()
    ui.setupUi(ScoresDlg)
    ScoresDlg.show()
    sys.exit(app.exec_())

