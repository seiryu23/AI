import analyzer
import dictionary
import FResponder
import random

class CCsMsc:

    def __init__(self, name):
        self.name = name
        self.dictionary = dictionary.Dictionary()
        self.emotion = Emotion(self.dictionary.pattern)
        self.res_repeat = FResponder.RepeatResponder('Repeat')
        self.res_random = FResponder.RandomResponder(
            'Random', self.dictionary.random
            )
        self.res_pattern = FResponder.PatternResponder(
            'Pattern', self.dictionary
            )


    def dialogue(self, input):
        self.emotion.update(input)
        parts = analyzer.analyze(input)
        ram = random.randint(1,100)
        if ram <= 40:
            self.responder = self.res_pattern
        elif 41 <= ram <= 90:
            self.responder = self.res_random
        else:
            self.responder = self.res_repeat
        resp = self.responder.response(input, self.emotion.mood)
        self.dictionary.study(input, parts)
        return resp

    def save(self):
        self.dictionary.save()

    def get_responder_name(self):
        return self.responder.name
    
    def get_name(self):
        return self.name

class Emotion:
    MOOD_MIN = -15
    MOOD_MAX = 15
    MOOD_RECOVERY = 0.5

    def __init__(self, pattern):
        self.pattern = pattern
        self.mood = 0
    
    def update(self, input):
        if self.mood < 0:
            self.mood += Emotion.MOOD_RECOVERY
        elif self.mood > 0:
            self.mood -= Emotion.MOOD_RECOVERY
        for ptn_item in self.pattern:
            if ptn_item.match(input):
                self.adjust_mood(ptn_item.modify)
                break
    
    def adjust_mood(self, val):
        self.mood += int(val)
        if self.mood > Emotion.MOOD_MAX:
            self.mood = Emotion.MOOD_MAX
        elif self.mood < Emotion.MOOD_MIN:
            self.mood = Emotion.MOOD_MIN
