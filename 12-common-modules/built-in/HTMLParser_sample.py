"""
Python提供了HTMLParser来非常方便地解析HTML
"""
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('start tag: <%s>, attr: %s' % (tag, attrs))

    def handle_endtag(self, tag):
        print('end tag: </%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('start end tag: <%s/>, attr: %s' % (tag, attrs))

    def handle_data(self, data):
        print("data:", data)

    def handle_comment(self, data):
        print('comment: <!--', data, '-->')

    def handle_entityref(self, name):
        print('entity ref: &%s;' % name)

    def handle_charref(self, name):
        print('char ref: &#%s;' % name)


parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')
