#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import sqlite3
from FlowSensor import FlowSensor
from Action import Action


class NfcSensor(Action):


    def __init__(self, name="NfcSensor"):
        super(NfcSensor, self).__init__(name)
        self.FlowSensor=[]
        self.FlowSensor.append(FlowSensor())



    def setup(self):

        #while True:

            tagID= "3444"
            conn = sqlite3.connect('/home/josep/Project_first_part-PIC-II/database.db')
            cursor = conn.execute("SELECT nfc from users where nfc=?" , (tagID,) )
            exist_nfc=cursor.fetchone()
            print "NFC DETECTAT:", exist_nfc
            print "Ja pots començar a beure"

            if exist_nfc != None:

                self.nfc = 1
                for a in self.FlowSensor:
                    a.setup(tagID)
                    a.get_data(tagID)

            else:
                self.nfc= 0



    def get_data():
        print self.values

    def  get_cumulative():
        pass

    def reset_cumulative():
        pass
        #reset sensor
