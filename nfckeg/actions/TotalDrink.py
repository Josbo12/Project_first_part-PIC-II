#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Action import Action
import sqlite3
from sensors import FlowSensor
import time

class TotalDrink(Action):
    """Total drink for BeerBoot"""
    def __init__(self):
        super(TotalDrink, self).__init__()


    def is_for_you(self,user):

        print "\nConsulta del usuari:", user
        conn1 = sqlite3.connect('/home/josep/Project_first_part-PIC-II/database.db')
        cursor1 = conn1.execute("SELECT user,nfc from users where user=?",(user,) )
        t=cursor1.fetchone()
        if t != None:
            data = [row for row in cursor1]
            iden=data[0]
            for a in iden:
                tagID=a

            conn = sqlite3.connect('/home/josep/Project_first_part-PIC-II/llistabeguts.db')
            cursor = conn.execute("SELECT id, quantitatbeguda from beguts where id=?",(tagID,))
            data2 = [row for row in cursor]
            quantitat_beguda=data2[0]
            for a in data2:
                for b in a:
                    self.TOTALBEGUT=b
            conn.close()
            return True
        else:
            return False


    def do(self,user):

        response= str("El ") + str(user) + str(" ha begut ") + str(self.TOTALBEGUT) + str(" cl")
        #print "\n", response
        return response
