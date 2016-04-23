import time

from NfcSensor import Nfcsensor as Nf

class FlowSensor():


    def __init__(self, name="FlowSensor"):
        super(FlowSensor, self).__init__(name)
        self.Nfcsensor=[]
        self.Nfcsensor.append(NfcSensor())




    def setup(self, nfc):

        for a in self.Nfcsensor:
            a.setup(nfc)

        delay = 5
        self.values=list()
        quantity_flow=0

        while self.nfc == "NFC OK":
            quantity_flow = 20 #sensor  #guarda les dades del sensor en una variable
            self.values.append(quantity_flow)
            time.sleep(5)

    def get_data():
        print self.values

    def  get_cumulative():
        pass

    def reset_cumulative()
        #reset sensor
