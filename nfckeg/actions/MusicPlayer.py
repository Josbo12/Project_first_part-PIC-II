from Action import Action
import sqlite3

class MusicPlayer(Action):
    """MusicPlayer for Ambrosio"""
    def __init__(self):
        super(MusicPlayer, self).__init__()
        #self.triggers = ["music", "audio"]
        #conn = sqlite3.connect('/home/josep/Project_first_part-PIC-II/database.db')
        #cursor = conn.execute("SELECT user from users")
        #data = [row for row in cursor]
        #self.hola = data
        #print self.hola[0]
        #print data[0]



    def is_for_you(self,user):
        conn = sqlite3.connect('/home/josep/Project_first_part-PIC-II/database.db')
        cursor = conn.execute("SELECT user from users where user=?",(user,) )
        #cursor = conn.execute("SELECT username, email from users where (username,email) values (?,?)",username, email )
        #t = [e for e in cursor]
        t=cursor.fetchone()

        print "printejo t = ", t
        conn.close()
        if t != None:
                return True
        else:
                return False

    def do(self, command):
        print "Will play music ", " ".join(command)
        return "OK"

    def is_for_yo4u(self, word):
        if word in self.hola:
            return True
        return False
