#!/usr/bin/python -uOO
# -*- coding: utf-8 -*-

######
##  Tadoku-Tan -- Offline Tadoku Reading Log
##  Tweet.py -- tie into the Twitter API to post updates
######

import twitter

CONSUMER_KEY = None
CONSUMER_KEY_SECRET = None
ACCESS_TOKEN = None
ACCESS_TOKEN_SECRET = None

# Create an interface with the Twitter API:
api = twitter.Api(consumer_key = CONSUMER_KEY,
                consumer_secret = CONSUMER_KEY_SECRET,
                access_token_key = ACCESS_TOKEN,
                access_token_secret = ACCESS_TOKEN_SECRET)

# Define constants for Twitter hashtags and the @ statement:
AT_STATEMENT = "@TadokuBot "
TIMES_HASH = {
    2 : "#second",
    3 : "#third",
    4 : "#fourth",
    5 : "#fifth",
}
TYPE_HASH = {
    "BOOK": "#book",
    "BKDR": "#book #dr",
    "MNGA": "#manga",
    "LYRC": "#lyrics",
    "WBPG": "#net",
    "NEWS": "#news",
    "FLGM": "#fullgame",
    "GAME": "#game",
    "NICO": "#nico",
    "SUBS": "#subs",
    "SENT": "#sentences",
}

def entryToTweet(entrytype, value, times = 1):
    # Given type, value, and times read, convert an entry to
    # the format expected by TadokuBot

    tweet = ""

    if entrytype in TYPE_HASH.keys():
        typetag = TYPE_HASH[entrytype]
    else:
        print "Error:  an entry type must be provided."
        return None

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
    tweet = AT_STATEMENT + valtag + " " + typetag + " " + timestag + ";"
    return tweet

def tweetEntry(tweet):
    # First check if Tadoku is active; if so, post the update to Twitter.
    try:
        if checkActiveTadoku():
            status = api.PostUpdate(tweet)
        else:
            print "Error:  TadokuBot is currently not open for submissions."
            status = None
        return status
    except twitter.TwitterError as tweet_err:
        print "Error: " + str(tweet_err)
        return None

def checkActiveTadoku():
    # Loads the TadokuBot's timeline, and reports whether the contest is open.
    # Due to limits in how much of the timeline can be retrieved, the contest is
    # assumed to be open unless a #close tag is found.

    contestopen = True
    closedate = None

    try:
        bottimeline = api.GetUserTimeline(id = "TadokuBot", count = 200)
    except twitter.TwitterError as tweet_err:
        print "Error:  " + str(tweet_err)
        return False

    for status in bottimeline:
        if status.text == "#open" and status.created_at > closedate:
            contestopen = True
        elif status.text == "#close":
            closedate = status.created_at
            contestopen = False

    return contestopen


## TESTS ##
if __name__ == "__main__":
    print entryToTweet("BOOK", 140, 2)
    print entryToTweet("MNGA", 156)
    print entryToTweet("SUBS", 454.5)
