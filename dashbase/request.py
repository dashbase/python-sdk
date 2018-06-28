import time


class QueryRequest(object):
    def __init__(self,
                 end_id=None,
                 start_id=None,
                 table=None,
                 query=None,
                 num=10,
                 fields=None,
                 disable_highlight=False,
                 time_from=None,
                 time_to=None,
                 aggs: dict = None
                 ):
        self.query = None
        if query is not None:
            self.query = {"queryType": "string", "queryStr": query}
        if aggs is not None:
            self.aggregations = aggs

        self.disableHighlight = disable_highlight
        self.endId = end_id
        self.startId = start_id
        self.tableNames = [table]
        self.numResults = num
        self.fields = fields
        if self.fields == "*":
            self.fields = ["*"]

        self.timeRangeFilter = {
            "startTimeInSec": time_from,
            "endTimeInSec": time_to,
        }

        if not self.timeRangeFilter["startTimeInSec"] and not self.timeRangeFilter["endTimeInSec"]:
            now = int(time.time())
            self.timeRangeFilter["startTimeInSec"] = now - 15 * 60
            self.timeRangeFilter["endTimeInSec"] = now

        if table is None:
            self.table = []

    def to_dict(self):
        return dict((k, v) for k, v in self.__dict__.items() if v)
