#!/usr/bin/python -uOO
# -*- coding: utf-8 -*-

######
##  Tadoku-Tan -- Offline Tadoku Reading Log
##  Config.py -- config handling class
######

import os
import ast
import logging
import ConfigParser

SCORING_DEFAULTS = {
    "book":         "1",
    "bookdr":       "1.48",
    "manga":        ".2",
    "lyric":        "1",
    "web":          "1",
    "news":         "1",
    "fullgame":     str(1.0/6.0),
    "game":         ".05",
    "nico":         ".1",
    "subs":         ".2",
    "sentences":    str(1.0/17.0),
}
OTHER_DEFAULTS = {
    "twitter":      "False",
    "language":     "'ja'",
}

class TadokuConfig(object):

    def __init__(self, filename = "tadoku.ini"):
        self.filename = filename
        self.config = None

    def createConfig(self):
        # Create a new config parser, fill with default values
        self.config = ConfigParser.ConfigParser()

        self.config.add_section("SCORING")
        self.config.add_section("OTHER")
        for item in SCORING_DEFAULTS.keys():
            self.config.set("SCORING", item, SCORING_DEFAULTS[item])
        for item in OTHER_DEFAULTS.keys():
            self.config.set("OTHER", item, OTHER_DEFAULTS[item])

    def updateConfig(self, newcfg):
        # Update the instance config with new values
        for item, value in newcfg.config.items("SCORING"):
            self.config.set("SCORING", item, value)
        for item, value in newcfg.config.items("OTHER"):
            self.config.set("OTHER", item, value)
            
        for item in SCORING_DEFAULTS.keys():
            vars(self)[item] = ast.literal_eval(self.config.get("SCORING", item))
        for item in OTHER_DEFAULTS.keys():
            vars(self)[item] = ast.literal_eval(self.config.get("OTHER", item))

    def loadConfig(self):
        # Make sure we actually have a config file to work with.
        try:
            assert(os.path.isfile(self.filename))
        except AssertionError, e:
            logging.error("Config load error: File does not exist.")

        # Make sure we have a default config; create one otherwise.
        if not self.config:
            self.createConfig()

        # Read config file, overwriting defaults where they differ
        self.config.read(self.filename)

        # Assign config values to instance variables. (Values are evaluated.)
        for item in SCORING_DEFAULTS.keys():
            vars(self)[item] = ast.literal_eval(self.config.get("SCORING", item))
        for item in OTHER_DEFAULTS.keys():
            vars(self)[item] = ast.literal_eval(self.config.get("OTHER", item))

    def saveConfig(self):
        try:
            with open(self.filename, 'w') as outfile:
                self.config.write(outfile)
                outfile.close()

        except IOError, ioerr:
            logging.error("Config save error: " + str(ioerr))
            