import requests

from dashbase.response import QueryResponse


class LowLevelClient(object):
    def __init__(self, host: str, token: str = None):
        self.headers = {'Accept': 'application/json'}
        if token:
            self.headers["io.dashbase.auth.token"] = token
        self.host = host
        self.verify = False

    def query(self, req, raw=False):
        path = "/v1/query"

        res = requests.post("{}{}".format(self.host, path), json=req.to_dict(), headers=self.headers,
                            verify=self.verify)
        res.raise_for_status()
        if raw:
            return res
        result = QueryResponse(res.json())
        result.parse()
        return result

    def cluster_info(self):
        path = "/v1/cluster/tables"
        res = requests.get("{}{}".format(self.host, path), headers=self.headers, verify=self.verify)
        res.raise_for_status()
        return res.json()

    def sql(self, sql):
        path = "/v1/sql"
        res = requests.get("{}{}".format(self.host, path), params={"sql": sql}, headers=self.headers,
                           verify=self.verify)
        res.raise_for_status()
        result = QueryResponse(res.json())
        result.parse()
        return result


class Client(LowLevelClient):
    def __init__(self, host: str, token: str = None):
        super().__init__(host, token)

    def topn(self, col, numFacets=5, table="*", sql=None):
        if sql is None:
            sql = 'SELECT TOPN("{col}", {numFacets}) as "values" FROM "{table}" LAST 15 MINUTES LIMIT 100'
        res = self.sql(sql=sql.format(col=col, numFacets=numFacets, table=table))
        return res.aggregations.get("values").get("facets")
