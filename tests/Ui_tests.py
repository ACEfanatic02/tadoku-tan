#!/usr/bin/python -uOO
# -*- coding: utf-8 -*-

######
##  Tadoku-Tan -- Offline Tadoku Reading Log
##  Ui_tests.py -- Ui unit-test suite
######

import unittest
import os
import sys
import datetime

sys.path.append("..")
from tadokutan import Ui

class TestMainWindow(unittest.TestCase):

    def setUp(self):
        self.window = Ui.MainWindow()
