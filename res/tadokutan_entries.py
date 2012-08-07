# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Bryan Taylor/Documents/ui/tadokutan_entries.ui'
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

class Ui_EntriesDlg(object):
	def setupUi(self, EntriesDlg):
		EntriesDlg.setObjectName(_fromUtf8("EntriesDlg"))
		EntriesDlg.setWindowModality(QtCore.Qt.ApplicationModal)
		EntriesDlg.resize(487, 249)
		EntriesDlg.setModal(True)
		self.buttonBox = QtGui.QDialogButtonBox(EntriesDlg)
		self.buttonBox.setGeometry(QtCore.QRect(390, 20, 81, 241))
		self.buttonBox.setOrientation(QtCore.Qt.Vertical)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
		self.entriesTable = QtGui.QTableWidget(EntriesDlg)
		self.entriesTable.setGeometry(QtCore.QRect(10, 10, 371, 221))
		self.entriesTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		self.entriesTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
		self.entriesTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
		self.entriesTable.setRowCount(1)
		self.entriesTable.setColumnCount(3)
		self.entriesTable.setObjectName(_fromUtf8("entriesTable"))
		self.entriesTable.horizontalHeader().setVisible(True)
		self.entriesTable.horizontalHeader().setDefaultSectionSize(120)
		self.entriesTable.horizontalHeader().setSortIndicatorShown(False)
		self.entriesTable.horizontalHeader().setStretchLastSection(True)
		self.entriesTable.verticalHeader().setVisible(False)
		self.removeButton = QtGui.QPushButton(EntriesDlg)
		self.removeButton.setGeometry(QtCore.QRect(390, 210, 91, 23))
		self.removeButton.setObjectName(_fromUtf8("removeButton"))

		self.retranslateUi(EntriesDlg)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), EntriesDlg.accept)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), EntriesDlg.reject)
		QtCore.QMetaObject.connectSlotsByName(EntriesDlg)

	def retranslateUi(self, EntriesDlg):
		EntriesDlg.setWindowTitle(QtGui.QApplication.translate("EntriesDlg", "Entries", None, QtGui.QApplication.UnicodeUTF8))
		self.removeButton.setText(QtGui.QApplication.translate("EntriesDlg", "Remove Entry", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	EntriesDlg = QtGui.QDialog()
	ui = Ui_EntriesDlg()
	ui.setupUi(EntriesDlg)
	EntriesDlg.show()
	sys.exit(app.exec_())

