#!/usr/bin/python -uOO
# -*- coding: utf-8 -*-

######
##  Tadoku-Tan -- Offline Tadoku Reading Log
##  Entries.py -- ui for entries dialog
######

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_EntriesDlg(object):

    def setupUi(self, EntriesDlg):
        # Dialog setup
        EntriesDlg.resize(500, 250)
        EntriesDlg.setWindowTitle(_fromUtf8("Entries"))
        EntriesDlg.setModal(True)

        # Ok/Cancel buttons
        self.buttonBox = QtGui.QDialogButtonBox(EntriesDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), EntriesDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), EntriesDlg.reject)

        # Entries table
        self.entriesTable = QtGui.QTableWidget(EntriesDlg)
        self.entriesTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.entriesTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.entriesTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.entriesTable.setRowCount(1)
        self.entriesTable.setColumnCount(3)

        self.entriesTable.horizontalHeader().setVisible(True)
        self.entriesTable.horizontalHeader().setDefaultSectionSize(120)
        self.entriesTable.horizontalHeader().setSortIndicatorShown(False)
        self.entriesTable.horizontalHeader().setStretchLastSection(True)

        self.entriesTable.verticalHeader().setVisible(False)

        # Button to remove entries
        self.removeButton = QtGui.QPushButton(EntriesDlg)
        self.removeButton.setText(_fromUtf8("Remove Entry"))

        self.setupLayout(EntriesDlg)

    def setupLayout(self, EntriesDlg):
        # Layout for button half:
        self.buttonLayout = QtGui.QVBoxLayout()
        self.buttonLayout.addWidget(self.buttonBox)
        self.buttonLayout.addWidget(self.removeButton)

        # Main layout:
        self.mainLayout = QtGui.QHBoxLayout(EntriesDlg)
        self.mainLayout.addWidget(self.entriesTable)
        self.mainLayout.addItem(self.buttonLayout)



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    EntriesDlg = QtGui.QDialog()
    ui = Ui_EntriesDlg()
    ui.setupUi(EntriesDlg)
    EntriesDlg.show()
    sys.exit(app.exec_())

