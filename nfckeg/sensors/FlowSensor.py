import time
import sqlite3


from Action import Action

class FlowSensor(Action):


    def __init__(self, name="FlowSensor"):
        super(FlowSensor, self).__init__(name)



    def setup(self,tagID):
        #i=3
        #self.quantitatbeguda=40
        #abc=True
        #print self.quantitatbeguda
        #return True

        #while abc==True:
        #    delay = 5
        #    values=[]
#
#            self.quantity_flow = i #sensor  #guarda les dades del sensor en una variable
#            values.append(self.quantity_flow)
#            time.sleep(3)       #segons entre lectura i lectura
#            print self.quantity_flow
#            i=i-1
#            if i==0:
#              break
            #delay = 5
            #self.values=list()



            quantity_flow = float(50) #sensor  #guarda les dades del sensor en una variable
            #self.values.append(quantity_flow)
            #time.sleep(5)       #segons entre lectura i lectura
            print quantity_flow
            conn = sqlite3.connect('/home/josep/Project_first_part-PIC-II/llistabeguts.db')
            cursor = conn.execute("SELECT id,quantitatbeguda from beguts where id=?" , (tagID,) )
            exist_nfc=cursor.fetchone()


            if exist_nfc == None:

                conn.execute('insert into beguts (id, quantitatbeguda)' +
                            'values (?, ?);',
                            (tagID,quantity_flow,))
                conn.commit()
            else:
                print cursor
                data = [row for row in cursor]
                #print "AIXO ES DATA"
                print len(data)
                id_quantitat=data[0]
                for a in id_quantitat:
                    print a
                quantitatbeguda=float(a)
                print "AIXO ES EL QUE HE BEGUT ABANS",a
                print "begut ara", quantity_flow
                self.TOTAL_begut= quantitatbeguda + quantity_flow
                print "total begut  =", self.TOTAL_begut
                conn.execute("UPDATE beguts set quantitatbeguda=? where id=?", (self.TOTAL_begut,tagID,))
                conn.commit()
                cursor = conn.execute("SELECT id, quantitatbeguda from beguts where id=?" , (tagID,))
                data = [row for row in cursor]
                print "data actualitzat",data



            conn.close()
            print "arribo"


    def get_data(self, tagID):
        pass


    def  get_cumulative():
        pass

    def reset_cumulative():
        pass
        #reset sensor
