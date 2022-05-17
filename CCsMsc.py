import FResponder
import random

class CCsMsc:

    def __init__(self, name):
        self.name = name
        self.res_random = FResponder.RandomResponder('Random')
        self.res_repeat = FResponder.RepeatResponder('Repeat')
        self.responder = self.res_repeat

    def dialogue(self, input):
        ram = random.randint(0,1)
        if ram == 0:
            self.responder = self.res_random
        else:
            self.responder = self.res_repeat
        return self.responder.response(input)
    
    def get_responder_name(self):
        return self.responder.name
    
    def get_name(self):
        return self.name