#!/usr/bin/python -uOO
# -*- coding: utf-8 -*-

import unittest
import sys
import time

# Console colors:
from pretty import printc, writec, switchColor

# Avoid bakemoji on windows:
# If you have your shell setup properly for ansi colors, just comment this out. 
if sys.platform.startswith('win32'):
    def printc(text, color): print text
    def writec(text, color): sys.stdout.write(text)
    def switchColor(color): pass


class ModuleTestRunner(object):
    """
    ModuleTestRunner

    Use addTest() to add individual TestCases
    Use addTestList() to add lists of TestCases

    modname = module name for test display
    """

    def __init__(self):
        object.__init__(self)
        self.tests = {}

    def addTest(self, modname, test):
        """ Adds a single unittest TestCase instance to
            be tested. """
        assert isinstance(test, unittest.TestCase)

        if modname in self.tests.keys():
            self.tests[modname].append(test)
        else:
            self.tests[modname] = [test]

    def addTestList(self, modname, testlist):
        """ Adds a list of unittest TestCases to be tested. """
        assert isinstance(testlist, list)

        for test in testlist:
            if not isinstance(test, unittest.TestCase):
                raise AttributeError("Invalid object provided.  All tests must be subclassed from unittest.TestCase.")

        if modname in self.tests.keys():
            for test in testlist:
                self.tests[modname].append(test)
        else:
            self.tests[modname] = testlist

    def run(self):
        """ Runs test suite. """
        fails = []
        err   = []
        skips = []
        count = 0

        writec("Running tests:\n", 'blue')

        start = time.time()

        for modname in self.tests.keys():

            mod = modname.upper() + ':'
            writec(mod.ljust(12), 'normal')

            for test in self.tests[modname]:
                result = unittest.TestResult()
                test.run(result)
                count += 1

                if result.errors:
                    err.append(result.errors)
                    writec('E', 'yellow')
                elif result.failures:
                    fails.append(result.failures)
                    writec('F', 'red')
                elif result.skipped:
                    skips.append(result.skipped)
                    writec('S', 'blue')
                else:
                    writec('.', 'green')

            writec('\n', 'normal')

        if len(err) > 0:
            print '\n------------\n'

            for msg in err:
                for e, m in msg:
                    writec("In "+str(e)+"\n", 'yellow')
                    writec(m, 'yellow')

        if len(fails) > 0:
            print '\n------------\n'

            for msg in fails:
                for e, m in msg:
                    writec("In "+str(e)+"\n", 'yellow')
                    writec(m, 'yellow')

        if len(skips) > 0:
            print '\n------------\n'

            for msg in skips:
                for e, m in msg:
                    writec("In "+str(e)+"\n", 'yellow')
                    writec(m, 'yellow')

        print '\n------------\n'

        stop = time.time()

        print "%d tests run in %f seconds, %d failures, %d skipped, %d unexpected errors." %(count, (stop - start), len(fails), len(skips), len(err))

