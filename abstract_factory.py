# code: utf-8
"""
created: 2017/2/26
"""


class AbstractDiagram(object):
    def __init__(self):
        self._text = []

    def show(self):
        print('I am abstract diagram: text= {}'.format(self._text))

    def add(self, text):
        self._text.append(text)


class ConcreteDiagram(AbstractDiagram):
    def show(self):
        print('I am concrete diagram: text= {}'.format(self._text))


class AbstractFactory(object):
    def make_diagram(self):
        return AbstractDiagram()

    def make_text(self, text):
        return 'abstract factory say {}'.format(text)


class ConcreteFactory(AbstractFactory):
    def make_diagram(self):
        return ConcreteDiagram()

    def make_text(self, text):
        return 'concrete factory say {}'.format(text)


def create_diagram(factory: AbstractFactory):
    diagram = factory.make_diagram()
    text = factory.make_text('hello')

    diagram.add(text)

    return diagram


def main():
    diagram1 = create_diagram(AbstractFactory())
    diagram1.show()

    diagram2 = create_diagram(ConcreteFactory())
    diagram2.show()


if __name__ == "__main__":
    main()
