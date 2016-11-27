"""
This is a work done by David Mutabazi
Email : info@caltbay.com
Phone: 18280075740
Location: Chengdu, China

"""

import feedparser
from flask import Flask

app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640',
             'rwanda': 'http://www.inyarwanda.com/articles/index.rss'}


@app.route("/")
@app.route("/bbc")
def bbc():
    return get_news('bbc')


@app.route("/rwanda")
def cnn():
    return get_news('rwanda').encode('utf-8')


@app.route("/igihe")
def igihe():
    return get_news('bbc')


@app.route("/iol")
def iol():
    return get_news('iol')


@app.route("/fox")
def fox():
    return get_news('fox')


body = """<html>
<body>
<h1>Headlines </h1>
<b>{0}</b> </ br>
<i>{1}</i> </ br>
<p>{2}</p> </ br>
<p> This was made by David </p>
</body>
</html> """


def get_news(publication):
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed['entries'][0]
    return u'body'.join((first_article.get("title"), first_article.
                         get("published"), first_article.get("summary"))).encode('utf-8')


if __name__ == "__main__":
    app.run(port=5000, debug=True)
