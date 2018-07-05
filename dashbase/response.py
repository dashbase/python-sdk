from schematics.models import Model
from schematics.types.base import StringType, BooleanType, BaseType, LongType
from schematics.types.compound import ListType, ModelType, DictType
from dashbase.request import Request


class Payload(Model):
    fields = DictType(ListType(StringType))
    stored = StringType()
    entities = ListType(BaseType)


class Hit(Model):
    timeInSeconds = LongType()
    globalId = LongType()
    payload = ModelType(Payload)  # type: Payload


class Response(Model):
    request: Request = ModelType(Request)
    totalDocs = LongType()
    numDocs = LongType()
    numHits = LongType()
    numDocsProcessed = LongType()
    numHitsProcessed = LongType()
    latencyInMillis = LongType()
    timeProcessedTo = LongType(default=0)
    isTimedOut = BooleanType(default=False)
    startId = StringType()
    endId = StringType()
    error = StringType()
    debugMap = DictType(BaseType)
    hits = ListType(ModelType(Hit))  # type: list[Hit]
    aggregations = DictType(BaseType)
    schema = DictType(StringType)


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
