#!/usr/bin/python -uOO
# -*- coding: utf-8 -*-

######
##  Tadoku-Tan -- Offline Tadoku Reading Log
##  Ui.py -- ui handling
######

import datetime
import logging
import os
import sys

# Import Ui pieces
from PyQt4.QtGui import *

from res.Ui.Main import Ui_MainWindow
#from res.tadokutan_newentry import Ui_MainWindow
from res.tadokutan_scores import Ui_ScoresDlg
from res.tadokutan_entries import Ui_EntriesDlg

import tadokutan.Log

class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Default the media type to book.
        self.ui.book_radio.setChecked(True)

        # Tie the enable/disable of DR checkbox to the book radio button.
        #self.ui.book_radio.toggled.connect(self.drTie)

        # Set a default filename
        self.filename = 'tadoku.sav'

        # Connect the buttons.
        self.ui.submitButton.clicked.connect(self.submitClick)
        self.ui.scoresButton.clicked.connect(self.scoresClick)
        self.ui.entriesButton.clicked.connect(self.entriesClick)

        # Pressing return in textbox triggers submit. 
        self.ui.amountRead.returnPressed.connect(self.submitClick)
        self.ui.timesRead.returnPressed.connect(self.submitClick)

        # Connect the file menu.
        self.ui.actionLoad.triggered.connect(self.fileLoad)
        self.ui.actionSave.triggered.connect(self.fileSave)
        self.ui.actionExit.triggered.connect(self.fileExit)

        # Create this session's Tadoku log, load the default file if it exists.
        self.tadokulog = tadokutan.Log.TadokuLog()
        if os.path.isfile(self.filename):
            self.tadokulog = self.tadokulog.load(self.filename)
        self.updateScore()

    def submitClick(self):
        # Take entry data, format it, and send to the active Tadoku log.
        timestamp = datetime.datetime.today()
        entrytype = self.getEntryType()
        value = self.parseVal(self.ui.amountRead.text(), entrytype)
        self.ui.amountRead.clear()
        if self.ui.timesRead.text():
            times = int(self.ui.timesRead.text()) - 1
            self.ui.timesRead.clear()
        else:
            times = 0

        self.tadokulog.addEntry(timestamp, entrytype, value, times)

        # After processing, update score display:
        self.updateScore()

        logging.info("Entry at " + str(timestamp) + ": " + str(value) + " " + entrytype)
        self.ui.statusbar.showMessage("Entry added.", 300)

        # Automatically save the file.  (This will be a config option in later versions.)
        self.tadokulog.save(self.filename)

    def scoresClick(self):
        # Opens the scores dialog and passes it a copy of the Tadoku log.
        scoredlg = ScoreDlg(self.tadokulog)

    def entriesClick(self):
        # Opens the entries dialog and passes it a copy of the Tadoku log.
        working = self.tadokulog.clone()
        entriesdlg = EntriesDlg(working)

        # If the entries dialog is closed with "OK", update the log with the changes.
        if entriesdlg.result():
            self.tadokulog = working

        self.updateScore()

    def parseVal(self, value, entrytype):
        # Parses values appropriately based on the entry type.
        if entrytype in ["BOOK", "BKDR",
                         "MNGA", "LYRC", 
                         "WBPG", "NEWS", 
                         "FLGM", "GAME", 
                         "SENT"]:
            return float(value)
        elif entrytype in ["NICO", "SUBS"]:
            # Parse times from HH:MM:SS to a float minutes value.
            hms = value.split(':')
            return (float(hms[0])*60.0) + (float(hms[1])) + (float(hms[2])/60.0)
        else:
            return 0

    def getEntryType(self):
        # Looks at the media radio buttons (and dr checkbox)
        # and returns a 4 character type code.
        if self.ui.book_radio.isChecked():
            if self.ui.dr_check.isChecked():
                return "BKDR"
            else:
                return "BOOK"
        elif self.ui.manga_radio.isChecked():
            return "MNGA"
        elif self.ui.lyric_radio.isChecked():
            return "LYRC"
        elif self.ui.net_radio.isChecked():
            return "WBPG"
        elif self.ui.news_radio.isChecked():
            return "NEWS"
        elif self.ui.flgame_radio.isChecked():
            return "FLGM"
        elif self.ui.game_radio.isChecked():
            return "GAME"
        elif self.ui.nico_radio.isChecked():
            return "NICO"
        elif self.ui.subs_radio.isChecked():
            return "SUBS"
        elif self.ui.sent_radio.isChecked():
            return "SENT"

    def updateScore(self):
        # Updates the total score display on the window.
        self.ui.total_score.setNum(round(self.tadokulog.getScore(), 2))

    def drTie(self):
        # If the book radio button is off, disable the double-row checkbox.
        if self.ui.book_radio.isChecked():
            self.ui.dr_check.setEnabled(True)
        else:
            self.ui.dr_check.setEnabled(False)

    def fileLoad(self):
        # Retrieves filename from dialog and loads file.
        fn = QFileDialog.getOpenFileName(self, "Load...", "", "Tadoku Saves (*.sav)")
        if fn:
            self.tadokulog = self.tadokulog.load(str(fn))
            self.updateScore()

            # Set this filename as the open file.
            self.filename = str(fn)

            self.ui.statusbar.showMessage("File loaded.", 300)
            logging.info("File loaded:  %s", fn)

    def fileSave(self):
        self.tadokulog.save(self.filename)
        self.ui.statusbar.showMessage("File saved.", 300)
        logging.info("File saved.")

    def fileExit(self):
        # Automatically saves (this will become a config option in later versions)
        # before exit.
        self.tadokulog.save(self.filename)
        logging.info("Program exit - File menu.")
        sys.exit()

class ScoreDlg(QDialog):

    def __init__(self, tadokulog):
        QDialog.__init__(self)

        self.tadokulog = tadokulog

        # Initiate Ui
        self.ui = Ui_ScoresDlg()
        self.ui.setupUi(self)

        self.ui.scores_radio.toggled.connect(self.update)
        self.ui.values_radio.toggled.connect(self.update)

        self.update()
        self.exec_()

    def update(self):
        # Update the score/value breakdowns.
        if self.ui.scores_radio.isChecked():
            self.ui.book_score.setNum(self.tadokulog.getScore(types = "BOOK"))
            self.ui.bookdr_score.setNum(self.tadokulog.getScore(types = "BKDR"))
            self.ui.manga_score.setNum(self.tadokulog.getScore(types = "MNGA"))
            self.ui.lyric_score.setNum(self.tadokulog.getScore(types = "LYRC"))
            self.ui.flgame_score.setNum(self.tadokulog.getScore(types = "FLGM"))
            self.ui.game_score.setNum(self.tadokulog.getScore(types = "GAME"))
            self.ui.net_score.setNum(self.tadokulog.getScore(types = "WBPG"))
            self.ui.news_score.setNum(self.tadokulog.getScore(types = "NEWS"))
            self.ui.nico_score.setNum(self.tadokulog.getScore(types = "NICO"))
            self.ui.subs_score.setNum(self.tadokulog.getScore(types = "SUBS"))
            self.ui.sent_score.setNum(self.tadokulog.getScore(types = "SENT"))

        elif self.ui.values_radio.isChecked():
            self.ui.book_score.setNum(self.tadokulog.getValue(types = "BOOK"))
            self.ui.bookdr_score.setNum(self.tadokulog.getValue(types = "BKDR"))
            self.ui.manga_score.setNum(self.tadokulog.getValue(types = "MNGA"))
            self.ui.lyric_score.setNum(self.tadokulog.getValue(types = "LYRC"))
            self.ui.flgame_score.setNum(self.tadokulog.getValue(types = "FLGM"))
            self.ui.game_score.setNum(self.tadokulog.getValue(types = "GAME"))
            self.ui.net_score.setNum(self.tadokulog.getValue(types = "WBPG"))
            self.ui.news_score.setNum(self.tadokulog.getValue(types = "NEWS"))
            self.ui.nico_score.setNum(self.tadokulog.getValue(types = "NICO"))
            self.ui.subs_score.setNum(self.tadokulog.getValue(types = "SUBS"))
            self.ui.sent_score.setNum(self.tadokulog.getValue(types = "SENT"))      

        # Update the total score.
        self.ui.total_score.setNum(self.tadokulog.getScore())

class EntriesDlg(QDialog):

    def __init__(self, tadokulog):
        QDialog.__init__(self)

        self.tadokulog = tadokulog

        # Initiate Ui
        self.ui = Ui_EntriesDlg()
        self.ui.setupUi(self)
        self.ui.entriesTable.setRowCount(1)
        self.ui.removeButton.clicked.connect(self.removeEntry)

        self.updateEntries()
        self.exec_()

    def updateEntries(self):
        # Fill the entry table from the tadoku log.
        row = 0

        entries = self.tadokulog.sortChrono()

        if not entries:
            self.ui.entriesTable.clearContents()

        #Turn off sorting so each entry will be placed together on the same row.
        self.ui.entriesTable.setSortingEnabled(False)

        # Expand table to fit.
        self.ui.entriesTable.setRowCount(len(entries))

        for item in entries:
            col = 0
            while col < 3:
                widgetitem = QTableWidgetItem(str(item[col]))
                widgetitem.setText(str(item[col]))
                self.ui.entriesTable.setItem(row, col, widgetitem)
                col += 1
            row += 1
            
        # Turn sorting back on.
        self.ui.entriesTable.setSortingEnabled(True)
        
    def removeEntry(self):
        # Remove the currently selected entry from the log.
        row = self.ui.entriesTable.currentRow()

        # Convert the string data back into a timestamp.
        t = self.ui.entriesTable.item(row, 0)
        timestamp = datetime.datetime.strptime(str(t.text()), "%Y-%m-%d %H:%M:%S.%f")

        # Undo entry and refresh the table.
        self.tadokulog.undoEntry(timestamp)
        self.updateEntries()

        logging.info("Entry removed.")
