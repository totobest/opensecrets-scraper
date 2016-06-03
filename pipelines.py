import os
from exporters import MyJSONEncoder


class JsonWriterPipeline(object):

    def __init__(self):
        directory = "output/"
        if not os.path.exists(directory):
            os.makedirs(directory)
        self.encoder = MyJSONEncoder()

    def process_item(self, item, spider):
        external_id = item.get("external_id")
        if external_id is None:
            return item

        f = open('output/{}.json'.format(external_id), 'wb')
        line = self.encoder.encode(dict(item)) + '\n'
        f.write(line)
        f.close()
        return item
