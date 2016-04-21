import time

class FlowSensor():


    def __init__(self, name="FlowSensor"):
        super(FlowSensor, self).__init__(name)


    def setup():

        read_value=True
        delay = S
        self.values=list()
        quantity_flow=0
        while read_value:
            quantity_flow = sensor #guarda les dades del sensor en una variable
            self.values.append(quantity_flow)
            time.sleep(S)

    def get_data():
        return self.values


    def  get_cumulative():
        pass

    def reset_cumulative()
        reset sensor
