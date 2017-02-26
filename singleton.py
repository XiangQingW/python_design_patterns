# coding: utf-8
"""

created: 2017/2/27
"""


class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance


class Single(Singleton):
    a = 1


def main():
    s1 = Single()
    s2 = Single()

    print(id(s1), id(s2))

    s2.a = 10
    print(s1.a, s2.a)

if __name__ == "__main__":
    main()
