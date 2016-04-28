import sys
import sqlite3
from Action import Action


class Database(Action):


    def __init__(self, cfg=None, name="Database"):
         super(Database, self).__init__(cfg, name)

    def save_data(self, cfg=None):

        conn = sqlite3.connect('/home/josep/Project_first_part-PIC-II/database.db')



        users = self.cfg["database"]["user"]
        for user in users:
            for usn in user:
                username = user[usn]['username']
                nfc = user[usn]['nfc']

                cursor = conn.execute("SELECT user, nfc, username from users where  user=? and nfc=? and username=?" ,(usn,nfc,username))
                t=cursor.fetchone()
                if t == None:
                    print "USUARIS AFEGITS:"
                    print usn, username, nfc
                    conn.execute('insert into users (user,nfc,username)' +
                                'values (?, ?, ?);',
                                (usn, nfc, username))
                else:
                    print "USUARIS NO AFEGITS"
                    print usn, username, nfc

        #user = user.strip()
        #nfc = self.cfg["database"]["nfc"]
        #username = self.cfg["database"]["username"]
        #conn.execute('insert into users (user,nfc,username)' +
        #            'values (?, ?, ?);',
        #            (user, nfc, username))
        #print ">%s<" %(nfc)
        conn.commit()
        conn.close()



    def get_data(self):
        conn = sqlite3.connect('/home/josep/Project_first_part-PIC-II/database.db')
        cursor = conn.execute("SELECT user,nfc,username from users")
        data = [row for row in cursor]
        #print data
        conn.close()
        return data
