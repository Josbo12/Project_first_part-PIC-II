import sys
import sqlite3



class Database():
    print "eiii"
    def save_data(self, user,nfc,username):

        conn = sqlite3.connect('nfcdatabase.db')
        cursor = conn.execute("SELECT user, nfc, username from users")
        aa=1
        print "adeu"
        for row in cursor:
            if row[0] == user:
                aa=2
                break
            if row[1] == nfc:
                aa=2
            if row[2] == username:
                aa==2
                break
        if aa == 1:
                conn.execute("insert into users (user,nfc,username) values (?, ?, ?)",
                         (user,
                          nfc,
                          username))
                conn.commit()
                conn.close()
                print "hola"

                return True
        else:
                return False
        print "hola11"


    def get_data():
        conn = sqlite3.connect('nfcdatabase.db')
        cursor = conn.execute("SELECT user,nfc,username from users")
        data = [row for row in cursor]
        conn.close()
        return data
