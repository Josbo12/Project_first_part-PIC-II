class Action(object):
    """Action to be carried on by nfckeg"""
    def __init__(self, name):
        super(Action, self).__init__()
        self.name = name
        #self.tagID = tagID

    def save_data(self, user, nfc, username):
        pass

    def get_data(self):
        pass
