from commandlist import CommandList
#import channels as ch
#import actions as ac
import time
import yaml
import json



class nfckeg(object):


    def __init__(self):
        super(nfckeg, self).__init__()
        self.cl = CommandList()

         self._get_config()
#        self.channels = []
#        self.channels.append(ch.TextChannel())
#        self.channels.append(ch.TelegramChannel())
#        self.actions = []
#        self.actions.append(ac.MusicPlayer())


    def _get_config(self):
        with open("nfckeg.yaml") as f:
            self.cfg = yaml.load(f)

        print "Configuracio: "
        print json.dumps(self.cfg, indent=4)


    def database():
