import random

class FResponder:
    def __init__(self, name):
        self.name = name
    
    def response(self, input):
        return ''

class RepeatResponder(FResponder):
    def response(self, input):
        return '{} とは？'.format(input)

class RandomResponder(FResponder):
    def __init__(self, name):
        super().__init__(name)
        self.responses = ['お疲れ様です', 'よろしくお願い致します', '左様でございますか', '大変恐縮です']

    def response(self, input):
        return (random.choice(self.responses))