

class nfckeg(object):




    def _get_config(self):
        with open("ambrosio.yaml") as f:
            self.cfg = yaml.load(f)

        print "Configuracio: "
        print json.dumps(self.cfg, indent=4)
