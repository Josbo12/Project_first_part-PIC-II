import time
import sqlite3

class NfcSensor():


    def __init__(self, name="NfcSensor"):
        super(NfcSensor, self).__init__(name)


    def setup(self, tagID):


        conn = sqlite3.connect('dadestask2.db')
        cursor = conn.execute("SELECT nfc from users where nfc=?" ,(tagID) )
        exist_nfc=cursor.fetchone()

        if exist_nfc != None:
            self.nfc = "NFC OK"
        else:
            self.nfc= "NFC WRONG"

    def get_data():
        print self.values

    def  get_cumulative():
        pass

    def reset_cumulative()
        #reset sensor
