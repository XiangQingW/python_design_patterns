# coding: utf-8
"""

created: 2017/02/27
"""


def main():
    print('***** html builder *****')
    html = create_form(HtmlBuilder())
    print(html)

    print('\n\n***** template builder *****')
    template = create_form(TemplateBuilder())
    print(template)


def create_form(builder):
    builder.add_title('this is title')
    builder.add_body('body 1')
    builder.add_body('body 2')
    builder.add_footer('this is footer')
    return builder.get_form()


class HtmlBuilder(object):
    def __init__(self):
        self.title = ''
        self.body = []
        self.footer = ''

    def get_form(self):
        html = '<title>{}</title>\n<body>{}</body>\n<footer>{}</footer>'
        return html.format(self.title, self.body, self.footer)

    def add_title(self, title):
        self.title = title

    def add_body(self, body):
        self.body.append(body)

    def add_footer(self, footer):
        self.footer = footer


class TemplateBuilder(HtmlBuilder):
    def get_form(self):
        template = 'title= {} body= {} footer= {}'
        return template.format(self.title, self.body, self.footer)


if __name__ == '__main__':
    main()
