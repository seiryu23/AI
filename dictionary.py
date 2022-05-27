import imp
import analyzer
import patternItem
import re

#クラス
class Dictionary(object):
    def __init__(self):
        self.random = self.makeRandomList()
        self.pattern = self.makePatternDictionary()
    
    def makeRandomList(self):
        #ファイルを読み込み文字列をすべて取得
        rfile = open('dics/random.txt', 'r', encoding = 'utf_8')
        r_lines = rfile.readlines()
        rfile.close()

        #取得した文字列を改行ごとに分割し配列として保持
        ramdomList = []
        for line in r_lines:
            str = line.rstrip('\n')
            if (str != ''):
                ramdomList.append(str)
        return ramdomList

    def makePatternDictionary(self):
        #ファイルを読み込み文字列をすべて取得
        pfile = open('dics/pattern.txt', 'r', encoding = 'utf_8')
        p_lines = pfile.readlines()
        pfile.close()

        #取得した文字列を改行ごとに分割し配列として保持
        patternList = []
        for line in p_lines:
            str = line.rstrip('\n')
            if (str != ''):
                patternList.append(str)
        
        patternItemList = []
        for pattern in patternList:
            ptn, prs = pattern.split('\t')
            patternItemList.append(patternItem.PatternItem(ptn, prs))
        return patternItemList

    def study(self, input, parts):
        input = input.rstrip('\n')
        self.study_random(input)
        self.study_pattern(input, parts)

    def study_random(self, input):
        if not input in self.random:
            self.random.append(input)

    def study_pattern(self, input, parts):
        for word, part in parts:
            if analyzer.keyword_check(part):
                depend = None
                for ptn_item in self.pattern:
                    if re.search(
                        ptn_item.pattern,
                        word
                        ):
                        depend = ptn_item
                        break
                if depend:
                    depend.add_phrase(input)
                else:
                    self.pattern.append(
                        patternItem.PatternItem(word, input)
                        )
    
    def save(self):
        for index, element in enumerate(self.random):
            self.random[index] = element + '\n'
        with open('dics/random.txt', 'w', encoding = 'utf_8') as f:
            f.writelines(self.random)
        pattern = []

        for ptn_item in self.pattern:
            pattern.append(ptn_item.make_line() + '\n')
        with open('dics/pattern.txt', 'w', encoding='utf_8') as f:
            f.writelines(pattern)