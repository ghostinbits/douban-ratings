#!/usr/bin/env python3

import re
import sys
import urllib.parse
import urllib.request


class Movie:

    def __init__(self, name):
        self.name = name

    def douban_rate(self):
        query = urllib.parse.urlencode([('cat', '1002'), ('q', name)])
        url = 'http://www.douban.com/search?{}'.format(query)
        response = urllib.request.urlopen(url).read().decode()
        rate = re.findall(r'(?<=<span class="rating_nums">)\d\.\d',
                          response)
        cast = re.findall(r'(?<=<span class="subject-cast">).*(?=</span>)',
                          response)
        return zip(cast, rate)


if __name__ == '__main__':
    try:
        name = sys.argv[1]
    except:
        name = input('Input a movie name: ')
    movie = Movie(name)
    for i in movie.douban_rate():
        print(' / '.join(i))
