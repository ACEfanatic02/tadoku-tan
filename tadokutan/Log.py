#!/usr/bin/python -uOO
# -*- coding: utf-8 -*-

######
##  Tadoku-Tan -- Offline Tadoku Reading Log
##  Log.py -- class container for the tadoku log
######

import datetime
import logging
import cPickle
import os

# Local Imports
import tadokutan.Config_new

class TadokuLog(object):
    ####
    # Class to store an instance of the Tadoku Log.
    # This allows for cleaner data management, while also
    # allowing, in a future version, the management of
    # multple Tadoku logs at once. (For Tadoku in multiple
    # languages or with multiple users)
    ####

    def __init__(self, cfg = None):
        object.__init__(self)

        # Holder for all entries, stored as tuples of 
        # (timestamp, entry type, entry value, times)
        self.entries = [ ]

        # If no config given, create one with default values.
        if cfg == None:
            self.cfg = tadokutan.Config.TadokuConfig()
            self.cfg.loadConfig()
        else:
            self.cfg = cfg

        # Fill the scoring table.
        self.SCORING = {
            "BOOK": self.cfg.book,
            "BKDR": self.cfg.bookdr,
            "MNGA": self.cfg.manga,
            "LYRC": self.cfg.lyric,
            "WBPG": self.cfg.web,
            "NEWS": self.cfg.news,
            "FLGM": self.cfg.fullgame,
            "GAME": self.cfg.game,
            "NICO": self.cfg.nico,
            "SUBS": self.cfg.subs,
            "SENT": self.cfg.sentences,
        }

    def clone(self):
        rv = TadokuLog(self.cfg)

        for item in self.entries:
            rv.addEntry(item[0], item[1], item[2], item[3])

        rv.SCORING = self.SCORING

        return rv

    def sortChrono(self):
        return sorted(self.entries, key = lambda entry:entry[0])

    def addEntry(self, timestamp, entrytype, value, times):
        self.entries.append((timestamp, entrytype, value, times))

    def undoEntry(self, timestamp = None):
        # If given a timestamp, deletes a particular entry.  
        # Otherwise deletes the last entry.
        entries = self.sortChrono() 

        if timestamp:
            for item in entries:
                if item[0] == timestamp:
                    entries.remove(item)
        else:
            entries.remove(entries[-1])

        self.entries = entries

    def getScore(self, types = [ ], timestamp = None):
        # Returns score totals by type.  If no type is given, returns total score overall.
        # Function designed by BlackDragonHunt.
        score = 0.0

        if timestamp:
            entries = self.sortChrono()
        else:
            entries = self.entries

        # If types is empty, fill it with all possible types.
        if not types:
            types = self.SCORING.keys()

        for item in entries:
            if timestamp and item[0] < timestamp:
                continue
            else:
                if item[1] in types and item[1] in self.SCORING:
                    score += (item[2] * self.SCORING[item[1]])/(2.0**item[3])

        return score

    def getValue(self, types = [ ], timestamp = None):
        # Returns value totals by type.  (i.e., pages read, minutes watched.)
        # If no type given, return 0.
        value = 0.0

        entries = self.entries

        if not types:
            return 0

        for item in entries:
            if timestamp and item[0] < timestamp:
                continue
            else:
                if item[1] in types:
                    value += item[2]

        return value

    def updateConfig(self, cfg):
        # Updates the scoring table according to the given config.
        self.SCORING = {
            "BOOK": cfg.book,
            "BKDR": cfg.bookdr,
            "MNGA": cfg.manga,
            "LYRC": cfg.lyric,
            "WBPG": cfg.web,
            "NEWS": cfg.news,
            "FLGM": cfg.fullgame,
            "GAME": cfg.game,
            "NICO": cfg.nico,
            "SUBS": cfg.subs,
            "SENT": cfg.sentences,
        }

    def save(self, fn = 'tadoku.sav'):
        # Pickles the class instance and writes to disk. 
        # Filename can be customized, but is defaulted to tadoku.sav

        try:
            with open(fn, 'wb') as f:
                cPickle.dump(self, f)
                f.close()
        except IOError as ioerr:
            logging.error("File write error: " + str(ioerr))

    def load(self, fn = 'tadoku.sav'):
        # Unpickles the class instance and returns it.
        # Filename can be customized, but is defaulted to tadoku.sav

        try:
            with open(fn, 'rb') as f:
                return cPickle.load(f)
        except IOError as ioerr:
            logging.error("File read error: " + str(ioerr))

