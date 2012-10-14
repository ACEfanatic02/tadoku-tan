#!/usr/bin/python -uOO
# -*- coding: utf-8 -*-

######
##  Tadoku-Tan -- Offline Tadoku Reading Log
##  tadokutan.py -- Main Scripts
######

import datetime
import sys
import logging

from PyQt4.QtGui import QApplication

# Local Imports
from tadokutan import Ui

# Configure logging system
logging.basicConfig(filename = "tadokutan.log",
                    level = logging.DEBUG, 
                    format = '%(asctime)s %(levelname)s : %(message)s')

# Launch program
app = QApplication(sys.argv, True)
main = Ui.MainWindow()

main.show()

sys.exit(app.exec_())
