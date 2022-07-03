from elasticsearch import Elasticsearch

from config import conf


class cicadaES:
    def __init__(self, index_name, index_type, host=conf.ES_HOST, port=conf.ES_PORT):
        self.es = Elasticsearch([{'host': host, 'port': port}], timeout=3600)
        self.index_name = index_name
        self.index_type = index_type

    def create_index(self):
        pass

    def delete_index(self):
        pass

    def get_doc(self):
        pass

    def insert_one(self, _id, doc):
        self.es.index(index=self.index_name,
                      doc_type=self.index_type, id=_id, body=doc)

    def search(self, query):
        return self.es.search(body=query)

    def insert_array(self, array):
        pass

    def update(self):
        pass
