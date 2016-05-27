from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import datetime

import re
from itertools import izip_longest, islice

import scrapy
from slugify import slugify


def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)


def smart_truncate(content, length=100, suffix='...'):
    if len(content) <= length:
        return content
    else:
        return ' '.join(content[:length+1].split(' ')[0:-1]) + suffix


def scrapy_strip(o):
    return o[0]

class OpenSecretsSpider(scrapy.Spider):
    name = 'opensecrets'
    start_urls = ['https://www.opensecrets.org/elections/']

    def parse(self, response):
        for title, definition in grouper(response.css('#rightColumn > *'), 2):
            # full_url = response.urljoin(href.extract())
            # yield scrapy.Request(full_url, callback=self.parse_definition)
            title = scrapy_strip(title.css('::text').extract())
            words = scrapy_strip(definition.css('::text').extract())

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
