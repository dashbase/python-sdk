import json
from dashbase.request import Request
from dashbase.response import  Response, ClusterOverviewResponse


def test_model():
    raw = """{
    "request": {
        "numResults": 1,
        "tableNames": [],
        "excludeTableNames": [],
        "query": {
            "queryType": "string",
            "queryStr": "Linux"
        },
        "timeRangeFilter": {
            "startTimeInSec": 1530784313,
            "endTimeInSec": 2147483647,
            "startGlobalId": 0,
            "endGlobalId": 9223372036854775807
        },
        "fields": [
            "agnet",
            "request",
            "agent",
            "offset"
        ],
        "aggregations": {},
        "useApproximation": false,
        "ctx": "93dfd003-4bf2-4800-a297-79cd16689bea",
        "fetchSchema": false,
        "timeoutMillis": 2147483647,
        "disableHighlight": false,
        "debugMode": 0
    },
    "totalDocs": 2621283522,
    "numDocs": 19947846,
    "numHits": 17618659,
    "numDocsProcessed": 11322,
    "numHitsProcessed": 10000,
    "latencyInMillis": 7,
    "timeProcessedTo": 1530784314,
    "isTimedOut": false,
    "startId": "nginx_json:0%3A5b3decdc",
    "endId": "nginx_json:0%3A5b3dea39",
    "debugMap": {},
    "hits": [
        {
            "timeInSeconds": 1530784988,
            "globalId": 6574671464962719616,
            "payload": {
                "fields": {
                    "request": [
                        "POST mobile.acme.com/mobile/data"
                    ],
                    "agent": [
                        "Dalvik/1.6.0 (<span class=\\"hl\\">Linux</span>; U; Android 4.4.4; ZTE A880 Build/KTU84P)"
                    ],
                    "offset": [
                        "5.201374729E9"
                    ]
                },
                "stored": "{\\"@timestamp\\":\\"2018-07-05T10:03:08.345Z\\",\\"offset\\":5201374729,\\"agent\\":\\"Dalvik/1.6.0 (Linux; U; Android 4.4.4; ZTE A880 Build/KTU84P)\\",\\"beat\\":{\\"name\\":\\"5a3dcc47c85b\\",\\"hostname\\":\\"5a3dcc47c85b\\",\\"version\\":\\"6.1.1\\"},\\"_subtable\\":\\"producer2\\",\\"response\\":200,\\"source\\":\\"/data/input/nginx_public.json\\",\\"bytesSent\\":853,\\"request\\":\\"POST mobile.acme.com/mobile/data\\",\\"host\\":\\"78.4.142.245\\"}",
                "entities": [
                    {
                        "highlight": {
                            "fields": {
                                "agent": [
                                    [
                                        {
                                            "offset": 31,
                                            "length": 5
                                        }
                                    ]
                                ]
                            },
                            "stored": [
                                {
                                    "offset": 84,
                                    "length": 5
                                }
                            ]
                        }
                    }
                ]
            }
        }
    ],
    "aggregations": {},
    "schema": {}
}"""
    data = json.loads(raw)
    req = Request(data["request"])
    req.validate()
    res = Response(data)
    res.validate()


def test_ClusterOverviewResponse():
    raw = """
    {"clusterPrefix":"docker","overview":{"nginx_json":{"metrics":{"system":{"cpuLoadFactor":2.2,"cpuUsagePercent":35.04406009335651,"numCores":8,"heapUsage":8511986456,"heapUsagePercent":49.546282133087516,"diskUsage":4370664448,"diskUsagePercent":0.1379402375132169},"indexing":{"numBytesPerSecond":24170504,"numBytesPerDay":2271156278400,"numEventsPerSecond":33865,"numEventsPerDay":3175804800},"query":{"avgLatencyMillis":0,"minLatencyMillis":0,"maxLatencyMillis":174,"p99LatencyMillis":1,"medianLatencyMillis":0,"queriesPerSecond":0},"isError":false},"info":{"0":["10.0.0.248:7888"],"1":["10.0.0.243:7888"]}}}}
    """
    data = json.loads(raw)
    req = ClusterOverviewResponse(data)
    req.values()

