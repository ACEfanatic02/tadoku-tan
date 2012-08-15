#!/usr/bin/python -uOO
# -*- coding: utf-8 -*-

######
##  Tadoku-Tan -- Offline Tadoku Reading Log
##  Log_tests.py -- TadokuLog unit-test suite
######

import unittest
import os
import sys
import datetime

sys.path.append("..")
from tadokutan import Log, Config_new as Config


class TestLog(unittest.TestCase):

    def setUp(self):
        cfg = Config.TadokuConfig(filename = "test.ini")
        cfg.loadConfig()
        self.log = Log.TadokuLog(cfg = cfg)
        self.filename = "tests/test.sav"

    def test_logconfig(self):
        # Assert that the contents of the log config are set to the proper defaults
        self.assertEqual(self.log.cfg.book, 1)
        self.assertEqual(self.log.cfg.bookdr, 1.48)
        self.assertEqual(self.log.cfg.manga, 0.2)
        self.assertEqual(self.log.cfg.lyric, 1)
        self.assertEqual(self.log.cfg.web, 1)
        self.assertEqual(self.log.cfg.news, 1)
        self.assertAlmostEqual(self.log.cfg.fullgame, 1.0/6.0)
        self.assertEqual(self.log.cfg.game, 0.05)
        self.assertEqual(self.log.cfg.nico, 0.1)
        self.assertEqual(self.log.cfg.subs, 0.2)
        self.assertAlmostEqual(self.log.cfg.sentences, 1.0/17.0)
        
        self.assertFalse(self.log.cfg.twitter)
        self.assertEqual(self.log.cfg.language, 'ja')

    def test_clone(self):
        self.log.addEntry(datetime.datetime.today(),"BOOK", 10, 1)

        clonelog = self.log.clone()

        for key in clonelog.SCORING.keys():
            self.assertAlmostEqual(self.log.SCORING[key], clonelog.SCORING[key],
                msg = "Different config values after clone.")

        self.assertEqual(self.log.entries, clonelog.entries,
                msg = "Different entries after clone.")

    def test_add(self):
        now = datetime.datetime.today()
        self.log.addEntry(now,"BOOK", 10, 1)

        self.assertEqual((now ,"BOOK", 10, 1), self.log.entries[0],
            msg = "Log entry not added successfully.")

    def test_undoWithTstmp(self):
        first = datetime.datetime.today()
        self.log.addEntry(first, "BOOK", 10, 1)
        second = datetime.datetime.today()
        self.log.addEntry(second, "BOOK", 20, 1)

        self.log.undoEntry(timestamp = first)
        self.assertEqual(self.log.entries[0], (second, "BOOK", 20, 1))

    def test_undoLast(self):
        first = datetime.datetime.today()
        self.log.addEntry(first, "BOOK", 10, 1)
        second = datetime.datetime.today()
        self.log.addEntry(second, "BOOK", 20, 1)

        self.log.undoEntry()
        self.assertEqual(self.log.entries[0], (first, "BOOK", 10, 1))

    def test_getScoreAll(self):
        now = datetime.datetime.today()

        self.log.addEntry(now, "MNGA", 20, 0)
        self.assertAlmostEqual(self.log.getScore(), 4)

        self.log.addEntry(now, "SUBS", 15, 0)
        self.assertAlmostEqual(self.log.getScore(), 7)

        self.log.addEntry(now, "BKDR", 20, 0)
        self.assertAlmostEqual(self.log.getScore(), 36.6)

    def test_getScoreByType(self):
        now = datetime.datetime.today()

        self.log.addEntry(now, "BOOK", 10, 0)
        self.log.addEntry(now, "BKDR", 10, 0)
        self.log.addEntry(now, "MNGA", 10, 0)
        self.log.addEntry(now, "LYRC", 10, 0)
        self.log.addEntry(now, "WBPG", 10, 0)
        self.log.addEntry(now, "NEWS", 10, 0)
        self.log.addEntry(now, "FLGM", 10, 0)
        self.log.addEntry(now, "GAME", 10, 0)
        self.log.addEntry(now, "NICO", 10, 0)
        self.log.addEntry(now, "SUBS", 10, 0)
        self.log.addEntry(now, "SENT", 10, 0)

        book_score  = self.log.getScore(types = ["BOOK"])
        bkdr_score  = self.log.getScore(types = ["BKDR"])
        manga_score = self.log.getScore(types = ["MNGA"])
        lyric_score = self.log.getScore(types = ["LYRC"])
        net_score   = self.log.getScore(types = ["WBPG"])
        news_score  = self.log.getScore(types = ["NEWS"])
        flgm_score  = self.log.getScore(types = ["FLGM"])
        game_score  = self.log.getScore(types = ["GAME"])
        nico_score  = self.log.getScore(types = ["NICO"])
        subs_score  = self.log.getScore(types = ["SUBS"])
        sent_score  = self.log.getScore(types = ["SENT"])

        self.assertEqual(book_score, 10)
        self.assertEqual(bkdr_score, 14.8)
        self.assertEqual(manga_score, 2)
        self.assertEqual(lyric_score, 10)
        self.assertEqual(net_score, 10)
        self.assertEqual(news_score, 10)
        self.assertAlmostEqual(flgm_score, (10.0/6.0))
        self.assertEqual(game_score, 0.5)
        self.assertEqual(nico_score, 1)
        self.assertEqual(subs_score, 2)
        self.assertAlmostEqual(sent_score, (10.0/17.0))

    def test_getValue(self):
        now = datetime.datetime.today()

        self.log.addEntry(now, "BOOK", 10, 0)
        self.log.addEntry(now, "BKDR", 10, 0)
        self.log.addEntry(now, "MNGA", 10, 0)
        self.log.addEntry(now, "LYRC", 10, 0)
        self.log.addEntry(now, "WBPG", 10, 0)
        self.log.addEntry(now, "NEWS", 10, 0)
        self.log.addEntry(now, "FLGM", 10, 0)
        self.log.addEntry(now, "GAME", 10, 0)
        self.log.addEntry(now, "NICO", 10, 0)
        self.log.addEntry(now, "SUBS", 10, 0)
        self.log.addEntry(now, "SENT", 10, 0)

        self.assertEqual(self.log.getValue(types = []), 0,
            msg = "If argument types is empty, should return 0")

        self.assertEqual(self.log.getValue(types = ["BOOK"]), 10)
        self.assertEqual(self.log.getValue(types = ["BKDR"]), 10)
        self.assertEqual(self.log.getValue(types = ["MNGA"]), 10)
        self.assertEqual(self.log.getValue(types = ["LYRC"]), 10)
        self.assertEqual(self.log.getValue(types = ["WBPG"]), 10)
        self.assertEqual(self.log.getValue(types = ["NEWS"]), 10)
        self.assertEqual(self.log.getValue(types = ["FLGM"]), 10)
        self.assertEqual(self.log.getValue(types = ["GAME"]), 10)
        self.assertEqual(self.log.getValue(types = ["NICO"]), 10)
        self.assertEqual(self.log.getValue(types = ["SUBS"]), 10)
        self.assertEqual(self.log.getValue(types = ["SENT"]), 10)

    def test_save(self):
        self.log.save(fn = self.filename)
        self.assertTrue(os.path.exists(self.filename))

    def test_load(self):
        self.log.save(fn = self.filename)
        self.assertTrue(isinstance(self.log.load(self.filename), Log.TadokuLog))

    def tearDown(self):
        if os.path.isfile("test.ini"):
            os.unlink("test.ini")
        if os.path.isfile(self.filename):
            os.unlink(self.filename)
        self.assertFalse(os.path.exists("test.ini"),
            msg = "TestLog: tear down failed; test.ini not deleted")
        self.assertFalse(os.path.exists(self.filename),
            msg = "TestLog: tear down failed; test.sav not deleted")
