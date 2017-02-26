# coding: utf-8
"""

created: 2017/2/27
"""
import copy


class Prototype(object):
    def __init__(self):
        self.value = ''

    def clone(self, **attrs):
        obj = copy.deepcopy(self)
        obj.__dict__.update(attrs)
        return obj


def main():
    proto = Prototype()

    a = proto.clone()
    b = proto.clone(value='b')
    c = proto.clone(value='c')

    print(a.value, b.value, c.value)


if __name__ == '__main__':
    main()
