# Scrapy settings for 16447541 project

SPIDER_MODULES = ['spiders']

FEED_EXPORTERS_BASE = {
    'my_json': 'exporters.MyJsonItemExporter'
}

FEED_FORMAT = "my_json"
FEED_URI = "export.json"
