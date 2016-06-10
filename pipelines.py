from io import BytesIO

import os
from exporters import MyJSONEncoder
from scrapy.pipelines.files import FSFilesStore, S3FilesStore
from six.moves.urllib.parse import urlparse


class JsonWriterPipeline(object):

    STORE_SCHEMES = {
        '': FSFilesStore,
        'file': FSFilesStore,
        's3': S3FilesStore,
    }

    def __init__(self, feed_uri):
        self.feed_uri = feed_uri
        self.encoder = MyJSONEncoder()
        self.store = self._get_store(self.feed_uri)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            feed_uri=crawler.settings.get('OUTPUT_URI'),
        )

    def _get_store(self, uri):
        if os.path.isabs(uri):  # to support win32 paths like: C:\\some\dir
            scheme = 'file'
        else:
            scheme = urlparse(uri).scheme
        store_cls = self.STORE_SCHEMES[scheme]
        return store_cls(uri)

    def process_item(self, item, spider):
        external_id = item.get("external_id")
        if external_id is None:
            return item

        buf = BytesIO()
        buf.writelines(self.encoder.encode(dict(item)) + '\n')
        buf.seek(0)
        path = '{}.json'.format(external_id)
        self.store.persist_file(path, buf, None)
        return item
