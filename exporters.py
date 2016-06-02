import datetime

from scrapy.exporters import JsonItemExporter
from scrapy.utils.serialize import ScrapyJSONEncoder


class MyJSONEncoder(ScrapyJSONEncoder):

    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.isoformat()
        else:
            return super(MyJSONEncoder, self).default(o)


class MyJsonItemExporter(JsonItemExporter):

    def __init__(self, file, **kwargs):
        super(MyJsonItemExporter, self).__init__(file, **kwargs)
        self.encoder = MyJSONEncoder()
