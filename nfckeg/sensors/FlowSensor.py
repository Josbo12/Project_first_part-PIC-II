import time


from Action import Action

class FlowSensor(Action):


    def __init__(self, name="FlowSensor"):
        super(FlowSensor, self).__init__(name)
        


    def setup(self):

        while True:
            delay = 5
            self.values=list()



            quantity_flow = 20 #sensor  #guarda les dades del sensor en una variable
            self.values.append(quantity_flow)
            time.sleep(5)       #segons entre lectura i lectura
            print quantity_flow

    def get_data():
        print self.values

    def  get_cumulative():
        pass

    def reset_cumulative():
        pass
        #reset sensor
