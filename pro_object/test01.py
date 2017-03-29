# -*- coding:utf-8 -*-

import urllib2
from HTMLParser import HTMLParser

import parser


class MovieParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.movies = []

    def handle_starttag(self, tag, attrs):

        def _attr(attrlist,attrname):
            for attr in attrlist:
                if attr[0] == attrname:
                    return attr[1]
            return None
        if tag == 'li'and _attr(attrs, 'data-title'):
            movie = {}
            movie['title'] = _attr(attrs, 'data-title')
            movie['score'] = _attr(attrs, 'data-score')
            movie['director'] = _attr(attrs, 'data-director')
            movie['actors'] = _attr(attrs, 'data-actors')
            self.movies.append(movie)
            print '%(title)s|%(score)s|%(director)s|%(actors)s' % movie


def nowplaying_movies(url):
    # type: (object) -> object
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    req = urllib2.Request(url, headers=headers)
    s = urllib2.urlopen(req)
    # print s.read()
    parser = MovieParser()
    parser.feed(s.read())
    return parser.movies


if __name__ == '__main__':
    url = 'https://movie.douban.com/nowplaying/hangzhou'
    movies = nowplaying_movies(url)
    print movies
    import json
    print('%s'% json.dumps(movies, sort_keys=True, indent=4, separators=(',',':')))