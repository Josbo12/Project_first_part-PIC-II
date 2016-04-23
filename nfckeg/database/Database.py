import sys
import sqlite3
from Action import Action


class Database(Action):
    print "eiii"

    def __init__(self, cfg=None, name="Database"):
         super(Database, self).__init__(cfg, name)

    def save_data(self, cfg=None):

        conn = sqlite3.connect('nfcdatabase.db')
        cursor = conn.execute("SELECT user, nfc, username from users")
        user = self.cfg["database"]["user"]
        nfc = self.cfg["database"]["nfc"]
        username = self.cfg["database"]["username"]
        conn.execute('insert into users (user,nfc,username)' +
                    'values (?, ?, ?);',
                    (user, nfc, username))
        conn.commit()
        conn.close()



    def get_data(self):
        conn = sqlite3.connect('nfcdatabase.db')
        cursor = conn.execute("SELECT user,nfc,username from users")
        data = [row for row in cursor]
        print data
        conn.close()
        return data
