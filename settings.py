# Scrapy settings for 16447541 project

SPIDER_MODULES = ['spiders']

FEED_EXPORTERS_BASE = {
    'json': 'exporters.MyJsonItemExporter'
}

FEED_FORMAT = None
FEED_URI = None

ITEM_PIPELINES = {
    'pipelines.JsonWriterPipeline': 0,
}