#!/usr/bin/python -uOO
# -*- coding: utf-8 -*-

######
##  Tadoku-Tan -- Offline Tadoku Reading Log
##  Config/tests.py -- Config unit-test suite
######

import unittest
import os
import sys

import tadokutan.Config_new as Config

class TestConfig(unittest.TestCase):

    def setUp(self):
        # Init class with test filename
        self.config = Config.TadokuConfig(filename = "test.ini")

    def test_create(self):
        self.config.createConfig()

        for option in self.config.config.options("SCORING"):
            assert(option in Config.SCORING_DEFAULTS.keys())
        for option in self.config.config.options("OTHER"):
            assert(option in Config.OTHER_DEFAULTS.keys())

    def test_save(self):
        if os.path.isfile(self.config.filename):
            os.unlink(self.config.filename)

        if not self.config.config:
            self.config.createConfig()

        self.config.saveConfig()

        assert(os.path.isfile == True)

    def test_load(self):
        if not os.path.isfile(self.config.filename):
            self.config.createConfig()
            self.config.saveConfig()

        self.config.loadConfig()

        for option in self.config.config.options("SCORING"):
            assert(option in Config.SCORING_DEFAULTS.keys())
        for option in self.config.config.options("OTHER"):
            assert(option in Config.OTHER_DEFAULTS.keys())

    def tearDown(self):
        # Delete the test file
        os.unlink(self.config.filename)