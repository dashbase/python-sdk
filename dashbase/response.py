class QueryResponse(object):
    def __init__(self, raw):
        self._parsed = False
        self.raw = raw
        self.hits = []
        self.end_id = None
        self.start_id = None
        self.num_hits = -1
        self.total_docs = -1
        self.aggregations = {}

    def parse(self):
        self.num_hits = self.raw['numHits']
        self.total_docs = self.raw['totalDocs']
        for hit in self.raw['hits']:
            obj = {
                '@timestamp': hit['timeInSeconds']
            }
            for key, value in hit["payload"]["fields"].items():
                obj[key] = value[0]
            self.hits.append(obj)
        if "startId" in self.raw:
            self.start_id = self.raw["startId"]

        if "endId" in self.raw:
            self.end_id = self.raw["endId"]

        self.aggregations = self.raw["aggregations"]
        self._parsed = True
