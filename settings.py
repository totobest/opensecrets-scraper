# Scrapy settings for 16447541 project

SPIDER_MODULES = ['spiders']

FEED_EXPORTERS_BASE = {
    'json': 'exporters.MyJsonItemExporter'
}

FEED_FORMAT = "json"

ITEM_PIPELINES = {
    'pipelines.JsonWriterPipeline': 0,
}


OUTPUT_URI = "output/"
# OUTPUT_URI = "s3://mybucket/output/"

# You can store your AWS credentials here. Uncomment the following:
# AWS_ACCESS_KEY_ID = ""
# AWS_SECRET_ACCESS_KEY = ""


# The maximum number of concurrent (ie. simultaneous) requests that will be performed by
# the Scrapy downloader.
#
# Default: 16
CONCURRENT_REQUESTS = 8

# The maximum number of concurrent (ie. simultaneous) requests that will be performed
# to any single domain.
#
# Default: 8

CONCURRENT_REQUESTS_PER_DOMAIN = CONCURRENT_REQUESTS


# Maximum number of concurrent items (per response) to process in parallel
# in the Item Processor (also known as the Item Pipeline).
#
# Default: 100

CONCURRENT_ITEMS = CONCURRENT_REQUESTS
