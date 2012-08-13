#!/usr/bin/python -uOO
# -*- coding: utf-8 -*-

######
##  Tadoku-Tan -- Offline Tadoku Reading Log
##  Config/tests.py -- Config unit-test suite
######

import unittest
import os
import sys
import logging

# HACK: append .. to path so we can import the main tadokutan module
sys.path.append("..")
from tadokutan import Config_new as Config

class TestConfig(unittest.TestCase):

    def setUp(self):
        # Init class with test filename
        self.config = Config.TadokuConfig(filename = "test.ini")
        logging.info("### TEST CONFIG SETUP ###")

    def test_create(self):
        logging.info("### TEST CONFIG CREATE ###")
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

        self.assertTrue(os.path.isfile(self.config.filename))

    def test_load(self):
        if not os.path.isfile(self.config.filename):
            self.config.createConfig()
            self.config.saveConfig()

        self.config.loadConfig()

        for option in self.config.config.options("SCORING"):
            assert(option in Config.SCORING_DEFAULTS.keys())
        for option in self.config.config.options("OTHER"):
            assert(option in Config.OTHER_DEFAULTS.keys())

        self.assertEqual(self.config.book, 1)
        self.assertEqual(self.config.bookdr, 1.48)
        self.assertEqual(self.config.manga, 0.2)
        self.assertEqual(self.config.lyric, 1)
        self.assertEqual(self.config.web, 1)
        self.assertEqual(self.config.news, 1)
        self.assertAlmostEqual(self.config.fullgame, 1.0/6.0)
        self.assertEqual(self.config.game, 0.05)
        self.assertEqual(self.config.nico, 0.1)
        self.assertEqual(self.config.subs, 0.2)
        self.assertAlmostEqual(self.config.sentences, 1.0/17.0)
        
        self.assertFalse(self.config.twitter)
        self.assertEqual(self.config.language, 'ja')

    def tearDown(self):
        # Delete the test file
        if os.path.isfile(self.config.filename):
            os.unlink(self.config.filename)
        self.assertFalse(os.path.exists(self.config.filename),
               msg = "TestConfig: tear down failed; test.ini not deleted.")

if __name__ == "__main__":
    unittest.main()