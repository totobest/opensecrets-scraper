from pytz import timezone
import datetime

from scrapy.exporters import JsonItemExporter
from scrapy.utils.serialize import ScrapyJSONEncoder


class MyJSONEncoder(ScrapyJSONEncoder):

    __utc_tz = timezone("UTC")

    def default(self, o):
        if isinstance(o, datetime.datetime):
            utc_dt = self.__utc_tz.localize(o)
            return utc_dt.strftime("%Y-%m-%dT%H:%M") + "+00:00"
        else:
            return super(MyJSONEncoder, self).default(o)


class MyJsonItemExporter(JsonItemExporter):

    def __init__(self, file, **kwargs):
        super(MyJsonItemExporter, self).__init__(file, **kwargs)
        self.encoder = MyJSONEncoder()
