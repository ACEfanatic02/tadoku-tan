#!/usr/bin/python -uOO
# -*- coding: utf-8 -*-

######
##  Tadoku-Tan -- Offline Tadoku Reading Log
##  run_tests.py -- main unit-test suite
######

import unittest
import datetime
import sys
import logging

sys.path.append(".")
from tests import Config_tests, Log_tests
from lib import test_runner

# filenames for tests, so we don't pollute the actual save and log:
now = datetime.datetime.today()
timestamp = now.isoformat('_')

# Suppress log messages on stderr
logging.basicConfig(level = logging.CRITICAL)


TEST_SAVE_FN = "tests/saves/test_"+str(timestamp)+".sav"

config_create = Config_tests.TestConfig('test_create')
config_save   = Config_tests.TestConfig('test_save')
config_load   = Config_tests.TestConfig('test_load')

log_cfg          = Log_tests.TestLog('test_logconfig')
log_clone        = Log_tests.TestLog('test_clone')
log_add          = Log_tests.TestLog('test_add')
log_undoTstmp    = Log_tests.TestLog('test_undoWithTstmp')
log_undoLast     = Log_tests.TestLog('test_undoLast')
log_getScoreAll  = Log_tests.TestLog('test_getScoreAll')
log_getScoreType = Log_tests.TestLog('test_getScoreByType')
log_getValue     = Log_tests.TestLog('test_getValue')
log_save         = Log_tests.TestLog('test_save')
log_load         = Log_tests.TestLog('test_load')

tadokutests = test_runner.ModuleTestRunner()


tadokutests.addTestList("Config", [config_create,
                                   config_save, 
                                   config_load])

tadokutests.addTestList("Log", [log_cfg, 
                                log_clone, 
                                log_add, 
                                log_undoTstmp, 
                                log_undoLast,
                                log_getScoreAll,
                                log_getScoreType,
                                log_getValue,
                                log_save,
                                log_load])

if __name__ == "__main__":
    # Run indivdual test suites
    tadokutests.run()