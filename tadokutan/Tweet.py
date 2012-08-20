#!/usr/bin/python -uOO
# -*- coding: utf-8 -*-

######
##  Tadoku-Tan -- Offline Tadoku Reading Log
##  Tweet.py -- tie into the Twitter API to post updates
######

import logging

# Define constants for Twitter hashtags and the @ statement:
AT_STATEMENT = "@TadokuBot "
TIMES_HASH = {
    2 : " #second",
    3 : " #third",
    4 : " #fourth",
    5 : " #fifth",
}
TYPE_HASH = {
    "BOOK": " #book",
    "BKDR": " #book #dr",
    "MNGA": " #manga",
    "LYRC": " #lyrics",
    "WBPG": " #net",
    "NEWS": " #news",
    "FLGM": " #fullgame",
    "GAME": " #game",
    "NICO": " #nico",
    "SUBS": " #subs",
    "SENT": " #sentences",
}

TWEET_MAX_LEN = 140

def entryToTweet(entrytype, value, times = 1):
    # Given type, value, and times read, convert an entry to
    # the format expected by TadokuBot

    tweet = ""

    if entrytype in TYPE_HASH.keys():
        typetag = TYPE_HASH[entrytype]
    else:
        raise ValueError("ERROR: A valid entrytype is required to create a tweet.")

    # Note that times read is not a required value, 
    # the bot will read the entry fine without it.
    if times in TIMES_HASH.keys():
        timestag = TIMES_HASH[times]
    # Handle the rare occasion of +5 times read:
    elif times > 5:
        timestag = TIMES_HASH[5]
    else:
        timestag = ""

    # Times must be formatted as HH:MM for the bot to accept them:
    if entrytype in ["SUBS", "NICO"]:
        t = int(value)
        m = t % 60
        if m < 10:
            m = "0" + str(m)
        t //= 60
        h = t
        valtag = str(h) + ":" + str(m)
    else:
        valtag = str(value)

    # Merge all tags together into a single tweet:
    # EX: "@TadokuBot 140 #book #second;"
    tweet = AT_STATEMENT + valtag + typetag + timestag + ";"

    # You'd have to do something incredibly stupid for
    # this to fail... but, sanity check:
    assert len(tweet) <= TWEET_MAX_LEN
    return tweet
