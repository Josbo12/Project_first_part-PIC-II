#!/usr/bin/env python
# -*- coding: utf-8 -*-

import database as db
import sensors as sen
import channels as ch
from commandlist import CommandList
from sensors import FlowSensor
import actions as ac
import sys
import yaml
import json
import time
#import time
#import yaml
#import json


#nfc = sys.argv[2]
#username = sys.argv[3]
class nfckeg(object):


        def __init__(self):
             super(nfckeg, self).__init__()

             #self.save_data(user, nfc, username)
             self.cl = CommandList()
             #self.save_data(user, nfc, username)
             self._get_config()
             self.database = []
             self.database.append(db.Database(self.cfg))
             self.channels = []
             #c = ch.TextChannel(self.cfg)
             #self.channels.append(c)
             self.channels.append(ch.TelegramChannel(self.cfgtel))

             self.sensors = []
             self.sensors.append(sen.NfcSensor())

             self.actions = []
             self.actions.append(ac.MusicPlayer())
             #self.sensors.append(sen.FlowSensor(tagID))
             #s
             #self.database.append(db.Database())
             for b in self.database:

               b.save_data(self.cfg) #guardar usuaris desde fitxer configuracio
               b.get_data() # mostrar tots els usuaris guardats
            #    break

             for a in self.sensors:

                a.setup() #guardar usuaris desde fitxer configuracio

                break


        def _get_config(self):
            with open("nfckeg.yaml") as f:
                self.cfg = yaml.load(f)
            with open ("telegram.yaml") as f1:
                self.cfgtel = yaml.load(f1)
            #print "Configuracio: "
            #print json.dumps(self.cfg, indent=4)
             #return response
        def next_command(self):
            try:
                return self.cl.next()
            except:
                return (None, None)

        def update_channels(self):
            for chan in self.channels:
                while chan.msg_avail():
                    self.cl.append((chan, chan.get_msg()))
        def execute_command(self, command):
            print "Will execute", command
            # Foreach Action in actions.
            #   if is_for_you()
            #       action.do
            words = command.split()
            print words
            first_word = words[0]
            rest_words = words[1:]
            response = None
            for a in self.actions:
                if a.is_for_you(first_word):
                    response = a.do(first_word)
                    break
            else:
                print "No t'entenc"
            return response

        def mainloop(self):
            # While True:
            #   command = get_command
            #   do_command(command)
            #   update
            while True:
                chan, command = self.next_command()
                if command:
                    response = self.execute_command(command)
                    chan.respond(response)

                time.sleep(1)
                self.update_channels()




a=0
if a==1:
        class nfckeg(object):


            def __init__(self):
                 super(nfckeg, self).__init__()
                 self.cl = CommandList()

                 self._get_config()
                 self.channels = []

                 self.channels.append(ch.TelegramChannel())
        #         self.actions = []
        #         self.actions.append(ac.MusicPlayer())

            def _get_config(self):
                with open("nfckeg.yaml") as f:
                    self.cfg = yaml.load(f)

                print "Configuracio: "
                print json.dumps(self.cfg, indent=4)


            def next_command(self):
                try:
                    return self.cl.next()
                except:
                    return (None, None)


            def update_channels(self):
                for chan in self.channels:
                    while chan.msg_avail():
                        self.cl.append((chan, chan.get_msg()))


            def execute_command(self, command):
                print "Will execute", command
                # Foreach Action in actions.
                #   if is_for_you()
                #       action.do
                words = command.split()
                first_word = words[0]
                rest_words = words[1:]
                response = "hola feo"
                for a in self.actions:
                    if a.is_for_you(first_word):
                        response = a.do(rest_words)
                        break
                else:
                    print "No t'entenc"
                return response

if __name__=="__main__":

    print "Gol"
    amb = nfckeg()
    amb.mainloop()
