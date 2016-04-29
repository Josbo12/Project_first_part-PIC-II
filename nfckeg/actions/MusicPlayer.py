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
        conn1 = sqlite3.connect('/home/josep/Project_first_part-PIC-II/database.db')
        cursor1 = conn1.execute("SELECT user,nfc from users where user=?",(user,) )
        t=cursor1.fetchone()
        data = [row for row in cursor1]
        print "AIXO ES DATA"
        print data
        iden=data[0]
        for a in iden:
            print a
            x=a

        print "aixo es x"
        print x
        print "AIXO ES iden"

        print iden




        #conn = sqlite3.connect('/home/josep/Project_first_part-PIC-II/llistabeguts.db')
        #cursor = conn.execute("SELECT id, quantitatbeguda from beguts where id=?",(self.data2,))
        #self.data = [row for row in cursor]
        #print "aixo es data"
        #print self.data



        #cursor = conn.execute("SELECT username, email from users where (username,email) values (?,?)",username, email )
        #t = [e for e in cursor]


        print "printejo t = ", t

        if t != None:
            self.data = [row for row in cursor1]
            print "OK"

            return True
        else:
                return False
        conn.close()

    def do(self, command):
        print "Will play music  ", " ".join(command)
        return "OK"

#######################################################################
    def is_for_yo4u(self, word):
        if word in self.hola:
            return True
        return False
