#!/usr/bin/python -uOO
# -*- coding: utf-8 -*-

######
##  Tadoku-Tan -- Offline Tadoku Reading Log
##  Tweet_tests.py -- Twitter functionality unit-test suite
######

import unittest
import os
import sys

# HACK: append .. to path so we can import the main tadokutan module
sys.path.append("..")
from tadokutan import Tweet

class TestTweet(unittest.TestCase):

    def setUp(self):
        pass

    def test_entryToTweet(self):
        entryA = ("BOOK", 100)
        entryB = ("MNGA", 20, 2)
        entryC = ("SUBS", 90)
        entryD = ("NICO", 61)

        tweetA = Tweet.entryToTweet(entryA[0], entryA[1])
        tweetB = Tweet.entryToTweet(entryB[0], entryB[1], times = entryB[2])
        tweetC = Tweet.entryToTweet(entryC[0], entryC[1])
        tweetD = Tweet.entryToTweet(entryD[0], entryD[1])

        self.assertEqual(tweetA, "@TadokuBot 100 #book;")
        self.assertEqual(tweetB, "@TadokuBot 20 #manga #second;")
        self.assertEqual(tweetC, "@TadokuBot 1:30 #subs;")
        self.assertEqual(tweetD, "@TadokuBot 1:01 #nico;")

    def test_errorHandling(self):
        self.assertRaises(ValueError, Tweet.entryToTweet, "", 100)

    def tearDown(self):
        pass
