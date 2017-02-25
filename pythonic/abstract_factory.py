# code: utf-8
"""
created: 2017/2/26
"""


class AbstractFactory(object):
    @classmethod
    def make_diagram(cls):
        return cls.Diagram()

    @classmethod
    def make_text(cls, text):
        return 'abstract factory say {}'.format(text)

    class Diagram(object):
        def __init__(self):
            self._text = []

        def show(self):
            print('I am abstract diagram: text= {}'.format(self._text))

        def add(self, text):
            self._text.append(text)


class ConcreteFactory(AbstractFactory):
    @classmethod
    def make_text(cls, text):
        return 'concrete factory say {}'.format(text)

    class Diagram(object):
        def __init__(self):
            self._text = []

        def show(self):
            print('I am concrete diagram: text= {}'.format(self._text))

        def add(self, text):
            self._text.append(text)


def create_diagram(factory: AbstractFactory):
    diagram = factory.make_diagram()
    text = factory.make_text('hello')

    diagram.add(text)

    return diagram


def main():
    diagram1 = create_diagram(AbstractFactory)
    diagram1.show()

    diagram2 = create_diagram(ConcreteFactory)
    diagram2.show()


if __name__ == "__main__":
    main()
