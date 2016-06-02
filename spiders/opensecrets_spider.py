from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import datetime
import itertools
from itertools import izip_longest

import re
import scrapy
from slugify import slugify


def grouper(iterable, n, fillvalue=None):
    """Collect data into fixed-length chunks or blocks"""
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)


def split_iter(string):
    return (x.group(0) for x in re.finditer(r"[^ ]+", string))


def smart_truncate(content, length=50, suffix='...'):
    words_list = list(itertools.islice(split_iter(content), length + 1))
    res = ' '.join(words_list[:length])
    return res + suffix if len(words_list) > length else res


class OpenSecretsSpider(scrapy.Spider):
    name = 'opensecrets'
    start_urls = ['https://www.opensecrets.org/elections/']

    def parse(self, response):
        for title, definition in grouper(response.css('#rightColumn > *'), 2):
            title = title.css('::text').extract()[0]
            words = definition.css('::text').extract()[0]

            yield {
                'abstract': smart_truncate(words, 50),
                'external_id': "opensecrets_{}".format(slugify(title, to_lower=True)),
                'date': datetime.datetime.today(),
                'title': title,
                'url': response.url,
                'words': words,
                'meta': {
                    'opensecrets': {

                    }
                }
            }
