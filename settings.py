# Scrapy settings for 16447541 project

SPIDER_MODULES = ['spiders']

FEED_EXPORTERS_BASE = {
    'json': 'exporters.MyJsonItemExporter'
}

FEED_FORMAT = "json"

ITEM_PIPELINES = {
    'pipelines.JsonWriterPipeline': 0,
}


OUTPUT_URI = "s3://mybucket/output/"

# You can store your AWS credentials here. Uncomment the following:
# AWS_ACCESS_KEY_ID = ""
# AWS_SECRET_ACCESS_KEY = ""

