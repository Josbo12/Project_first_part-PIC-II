#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import sqlite3


from Action import Action

class FlowSensor(Action):


    def __init__(self, name="FlowSensor"):
        super(FlowSensor, self).__init__(name)



    def setup(self,tagID):


            #while tagID != None:
                self.quantity_flow = float(50) #sensor guarda les dades del sensor en una variable
                #self.values.append(quantity_flow)

                #time.sleep(5)       #segons entre lectura i lectura
                print " \nQuantitat beguda ara:",self.quantity_flow
            # begut = self.values[len(self.values-1)]-self.values(0)  ultima quantita registrada
                                                                    # menys la primera registrada

    def get_data(self, tagID):


        conn = sqlite3.connect('/home/josep/Project_first_part-PIC-II/llistabeguts.db')
        cursor = conn.execute("SELECT id,quantitatbeguda from beguts where id=?" , (tagID,) )
        exist_nfc=cursor.fetchone()

        if exist_nfc == None:

            conn.execute('insert into beguts (id, quantitatbeguda)' +
                        'values (?, ?);',
                        (tagID,self.quantity_flow,))
            conn.commit()
        else:
            data = [row for row in cursor]
            id_quantitat=data[0]
            for a in id_quantitat:
                print ""
            quantitatbeguda=float(a)
            Total_begut= quantitatbeguda + self.quantity_flow
            print "En total has begut: ", Total_begut
            conn.execute("UPDATE beguts set quantitatbeguda=? where id=?", (Total_begut,tagID,))
            conn.commit()
        conn.close()


    def  get_cumulative():
        pass

    def reset_cumulative():
        pass
        #reset sensor
