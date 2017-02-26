# coding: utf-8
"""

created: 2017/2/27
"""


class ChineseGetter(object):
    def __init__(self):
        self.words = {
            'this': '这',
            'is': '是',
            'a': '一只',
            'dog': '狗'
        }

    def get(self, word):
        return self.words.get(word)


class EnglishGetter(object):
    def get(self, word):
        return word


def get_getter(language):
    getter = {
        'chinese': ChineseGetter,
        'english': EnglishGetter
    }

    return getter[language]()

if __name__ == '__main__':
    chinese, english = get_getter('chinese'), get_getter('english')

    for word in 'this is a dog'.split(' '):
        print(english.get(word), chinese.get(word))
