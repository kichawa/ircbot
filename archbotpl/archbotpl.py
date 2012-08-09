#!/usr/bin/env python
#import sys
#import os
#import optparse
import irclib
import ircbot
irclib.DEBUG = True
network = 'irc.freenode.net'
port = 6667
channel = '#mojtest'
nick = 'archbotpl'
name = 'archlinux.pl'
# Create a dictionary to store statistics in
statistics = {}
import feedparser
furl = "http://archlinux.pl/forum/feeds/forum/16/"
f = feedparser.parse(furl)
for a in f:
    print a
# Create our bot class
class StatBot ( ircbot.SingleServerIRCBot ):

   # Join the channel when welcomed
   def on_welcome ( self, connection, event ):

      connection.join ( channel )

   # React to channel messages
   def on_pubmsg ( self, connection, event ):

      source = event.source().split ( '!' ) [ 0 ]

      # Check to see if the user has queried us
      if event.arguments() [ 0 ].upper() == '!STATBOT':

         # Check to see if the user is in the dictionary
         if statistics.has_key ( source ):

            # Message the user his or her statistics
            connection.privmsg ( source, 'You have sent ' + str
( statistics [ source ] ) + ' lines.' )

         # Message the user saying that we have no record
         else:
            connection.privmsg ( source, 'I have no record ofyou.' )

      # A regular message has been sent to us
      else:

         # Add the user to the dictionary is necessary
         if not statistics.has_key ( source ):
            statistics [ source ] = 0

         # Add a line
         statistics [ source ] = statistics [ source ] + 1

# Create the bot
bot = StatBot ( [( network, port )], nick, name )
bot.start()
"""irc = irclib.IRC()
server = irc.server()
server.connect(network, port, nick, ircname = name)
server.join(channel)
server.privmsg ( channel, 'PRIVMSG to a channel.' )"""
"""lastspeaker = None
def handlePubMessage(connection, event):
        global lastspeaker
        target = event.target()
        speaker = event.source().split('!')[0]
        msg = event.arguments()[0]
        print target, ">", speaker, ":", msg
        p = os.popen("festival --tts", "w")
        if speaker != lastspeaker:
                p.write(speaker + " says ")
        p.write(msg)
        p.close()
        lastspeaker = speaker
irc.add_global_handler('pubmsg', handlePubMessage)"""
#irc.process_forever()
