#!/usr/bin/python -uOO
# -*- coding: utf-8 -*-

######
##	Tadoku-Tan -- Offline Tadoku Reading Log
##	TadokuConfig.py -- config handling class
######

import os
import ast
import logging
import ConfigParser

SCORING_DEFAULTS = {
	"book":			"1",
	"bookdr":		"1.48",
	"manga":		".2",
	"lyric": 		"1",
	"web": 			"1",
	"news":			"1",
	"fullgame":		str(1.0/6.0),
	"game":			".05",
	"nico":			".1",
	"subs":			".2",
	"sentences":	str(1.0/17.0),
}
OTHER_DEFAULTS = {
	"twitter": 		"False",
	"language":		"ja"
}

class TadokuConfig:
	def __init__(self, filename = "tadoku.ini"):
		# If the config file does not exist, create it with default values.
		# Otherwise, load the config.
		self.filename = filename
		if not os.path.isfile(self.filename):
			self.saveConfig()
		self.loadConfig()

	def loadConfig(self):
		# Create an empty config.
		config = ConfigParser.ConfigParser()

		# Set defaults.
		config.add_section("SCORING")
		config.add_section("OTHER")
		for item in SCORING_DEFAULTS.keys():
			config.set("SCORING", item, SCORING_DEFAULTS[item])
		for item in OTHER_DEFAULTS.keys():
			config.set("OTHER", item, OTHER_DEFAULTS[item])

		# Then read the file into it.
		config.read(self.filename)

		# Assign config values to instance variables. 
		# Values are converted to numeric values rather than strings.
		for item in SCORING_DEFAULTS.keys():
			vars(self)[item] = ast.literal_eval(config.get("SCORING", item))
		for item in OTHER_DEFAULTS.keys():
			vars(self)[item] = ast.literal_eval(config.get("OTHER", item))

	def saveConfig(self):

		# Are we creating a new file from the defaults, or saving our instance?
		if os.path.isfile(self.filename):
			createnew = False
		else:
			createnew = True
			
		try:
			with open(self.filename, 'w') as outfile:
				# Create an empty config with our sections:
				config = ConfigParser.ConfigParser()
				config.add_section("SCORING")
				config.add_section("OTHER")

				# Fill with defaults or instance variables as necessary:
				if createnew:
					for item in SCORING_DEFAULTS.keys():
						config.set("SCORING", item, SCORING_DEFAULTS[item])
					for item in OTHER_DEFAULTS.keys():
						config.set("OTHER", item, OTHER_DEFAULTS[item])
				else:
					for item in SCORING_DEFAULTS.keys():
						config.set("SCORING", item, str(vars(self)[item]))
					for item in OTHER_DEFAULTS.keys():
						config.set("OTHER", item, str(vars(self)[item]))

				config.write(outfile)

				outfile.close()
		except IOError as ioerr:
			logging.error("Config creation error: " + str(ioerr))

