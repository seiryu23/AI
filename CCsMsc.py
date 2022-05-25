import analyzer
import dictionary
import FResponder
import random

class CCsMsc:

    def __init__(self, name):
        self.name = name
        self.dictionary = dictionary.Dictionary()
        self.res_repeat = FResponder.RepeatResponder('Repeat')
        self.res_random = FResponder.RandomResponder(
            'Random', self.dictionary.random
            )
        self.res_pattern = FResponder.PatternResponder(
            'Pattern', self.dictionary
            )


    def dialogue(self, input):
        parts = analyzer.analyze(input)
        ram = random.randint(1,100)
        if ram <= 40:
            self.responder = self.res_pattern
        elif 41 <= ram <= 90:
            self.responder = self.res_random
        else:
            self.responder = self.res_repeat
        resp = self.responder.response(input)
        self.dictionary.study(input, parts)
        return resp

    def save(self):
        self.dictionary.save()

    def get_responder_name(self):
        return self.responder.name
    
    def get_name(self):
        return self.name