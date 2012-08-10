#!/usr/bin/python -uOO
# -*- coding: utf-8 -*-

######
##  Tadoku-Tan -- Offline Tadoku Reading Log
##  run_tests.py -- main unit-test suite
######

import unittest
import datetime

# filenames for tests, so we don't pollute the actual save and log:
now = datetime.datetime.today()
timestamp = now.isoformat('_')

TEST_SAVE_FN = "/tests/saves/test_"+str(timestamp)+".sav"
TEST_LOG_FN  = "/tests/logs/test_"+str(timestamp)+".log"

if __name__ == "__main__":
    # Run indivdual test suites