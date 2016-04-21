from commandlist import CommandList

import sensor as sen
import channels as ch
#import actions as ac
import time
import yaml
import json



class nfckeg(object):


    def __init__(self):
        super(nfckeg, self).__init__()
        self.cl = CommandList()

         self._get_config()
         self.channels = []

         self.channels.append(ch.TelegramChannel())
#         self.actions = []
#         self.actions.append(ac.MusicPlayer())

    def _get_config(self):
        with open("nfckeg.yaml") as f:
            self.cfg = yaml.load(f)

        print "Configuracio: "
        print json.dumps(self.cfg, indent=4)


    def next_command(self):
        try:
            return self.cl.next()
        except:
            return (None, None)


    def update_channels(self):
        for chan in self.channels:
            while chan.msg_avail():
                self.cl.append((chan, chan.get_msg()))


    def execute_command(self, command):
        print "Will execute", command
        # Foreach Action in actions.
        #   if is_for_you()
        #       action.do
        words = command.split()
        first_word = words[0]
        rest_words = words[1:]
        response = None
        for a in self.actions:
            if a.is_for_you(first_word):
                response = a.do(rest_words)
                break
        else:
            print "No t'entenc"
        return response


    def mainloop(self):
        # While True:
        #   command = get_command
        #   do_command(command)
        #   update

        target_detected = True
        while target_detected:
            #detectem una targeta
            for s in self.sensors:
                














if __name__ == "__main__":
    print "Start drinking"
    NFC = nfckeg()
    NFC.mainloop()
