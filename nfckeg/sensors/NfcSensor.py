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

        tagID= "999988882"
        conn = sqlite3.connect('/home/josep/Project_first_part-PIC-II/database.db')
        cursor = conn.execute("SELECT nfc from users where nfc=?" , (tagID,) )
        exist_nfc=cursor.fetchone()
        print "setupnfc", exist_nfc

        if exist_nfc != None:

            self.nfc = 1
            for a in self.FlowSensor:
                a.setup()
        else:
            self.nfc= 0

    def get_data():
        print self.values

    def  get_cumulative():
        pass

    def reset_cumulative():
        pass
        #reset sensor
