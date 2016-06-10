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
    start_urls = ['https://www.opensecrets.org/']

    def parse(self, response):

        for category in response.css('#nav a::attr(href)'):
            full_url = response.urljoin(category.extract())
            yield scrapy.Request(full_url, callback=self.parse_page)

    def parse_page(self, response):

        title_selector_list = [
            '#landingIntro h1::text',
            '#pageHeading::text',
            '#rightColumn h1::text'
        ]

        title_extractor_list = itertools.imap(
            lambda selector: " ".join(response.css(selector).extract()).strip(),
            title_selector_list
        )
        title = next(candidate_title for candidate_title in title_extractor_list if candidate_title)

        text_selector_list = [
            '#landingIntro p::text',
            '#rightColumn h2::text,#rightColumn h3::text,#rightColumn a::text,'
            '#rightColumn div::text,#rightColumn p::text,#rightColumn span::text'
        ]

        text_extractor_list = itertools.imap(
            lambda selector: " ".join(response.css(selector).extract()).strip(),
            text_selector_list
        )
        text = " ".join(candidate_text for candidate_text in text_extractor_list if candidate_text).strip()

        url = response.url

        data = {
                'abstract': smart_truncate(text, 50),
                'external_id': "opensecrets_{}".format(slugify(title, to_lower=True)),
                'date': datetime.datetime.today(),
                'title': title,
                'url': url,
                'words': text,
                'meta': {
                    'opensecrets': {

                    }
                }
            }
        yield data

        for section in response.css('#leftNavList a::attr(href)'):
            full_url = response.urljoin(section.extract())
            if not full_url.startswith("javascript:"):
                yield scrapy.Request(full_url, callback=self.parse_page)
