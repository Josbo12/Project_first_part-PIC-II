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

#self.set_nfcuser=sys.argv4[1]

class nfckeg(object):


        def __init__(self):
             super(nfckeg, self).__init__()


             self.cl = CommandList()
             self._get_config()
             self.database = []
             self.database.append(db.Database(self.cfg))
             self.channels = []
             self.channels.append(ch.TelegramChannel(self.cfgtel))
             self.sensors = []
             self.sensors.append(sen.NfcSensor())
             self.actions = []
             self.actions.append(ac.TotalDrink())

             for b in self.database:

               b.save_data(self.cfg)     #guardar usuaris des del fitxer de configuració
               b.get_data()
               # b.set_data(self.set_nfcuser)


             for a in self.sensors:

                a.setup() #activar sensor NFC
                break


        def _get_config(self):
            with open("nfckeg.yaml") as f:
                self.cfg = yaml.load(f)
            with open ("telegram.yaml") as f1:
                self.cfgtel = yaml.load(f1)


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
            words = command.split()
            print words
            first_word = words[0]
            rest_words = words[1:]
            response = None
            for a in self.actions:
                if a.is_for_you(first_word):
                    response = a.do(first_word)
                    break
            return response

        def mainloop(self):
            while True:
                chan, command = self.next_command()
                if command:
                    response = self.execute_command(command)
                    chan.respond(response)

                time.sleep(1)
                self.update_channels()


if __name__=="__main__":

    amb = nfckeg()
    amb.mainloop()
