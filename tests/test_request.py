import json
from dashbase.request import Request
from dashbase.response import  Response


def test_model():
    raw = """{
    "request": {
        "numResults": 1,
        "tableNames": [],
        "excludeTableNames": [],
        "timeRangeFilter": {
            "startTimeInSec": 1530691746,
            "endTimeInSec": 1530692646,
            "startGlobalId": 0,
            "endGlobalId": 9223372036854775807
        },
        "fields": [
            "*"
        ],
        "aggregations": {
            "FILTER.TS.MAX": {
                "requestType": "numeric",
                "col": "bytesSent",
                "type": "count"
            }
        },
        "useApproximation": false,
        "ctx": "1bd3563834aa1376",
        "fetchSchema": false,
        "timeoutMillis": 2147483647,
        "disableHighlight": false,
        "debugMode": 0
    },
    "totalDocs": 2790111152,
    "numDocs": 26861394,
    "numHits": 26861394,
    "numDocsProcessed": 26861394,
    "numHitsProcessed": 26861394,
    "latencyInMillis": 582,
    "timeProcessedTo": 1530691775,
    "isTimedOut": false,
    "startId": "nginx_json:0%3A5b3c83d1",
    "endId": "nginx_json:0%3A5b3c80be",
    "debugMap": {},
    "hits": [
        {
            "timeInSeconds": 1530692561,
            "globalId": 6574274494020452224,
            "payload": {
                "fields": {
                    "beat.name": [
                        "cb7fa5869eaf"
                    ],
                    "beat.hostname": [
                        "cb7fa5869eaf"
                    ],
                    "request": [
                        "POST mobile.acme.com/mobile/data"
                    ],
                    "agent": [
                        "Dalvik/1.6.0 (Linux; U; Android 4.2.2; GN9000 Build/JDQ39)"
                    ],
                    "offset": [
                        "1.020038216E9"
                    ],
                    "response": [
                        "200.0"
                    ],
                    "host": [
                        "70.204.104.46"
                    ],
                    "source": [
                        "/data/input/nginx_public.json"
                    ],
                    "bytesSent": [
                        "867.0"
                    ],
                    "beat.version": [
                        "6.1.1"
                    ],
                    "_subtable": [
                        "doc",
                        "producer3"
                    ]
                },
                "stored": "{\\"@timestamp\\":\\"2018-07-04T08:22:41.416Z\\",\\"host\\":\\"70.204.104.46\\",\\"response\\":200,\\"_subtable\\":\\"producer3\\",\\"beat\\":{\\"name\\":\\"cb7fa5869eaf\\",\\"hostname\\":\\"cb7fa5869eaf\\",\\"version\\":\\"6.1.1\\"},\\"bytesSent\\":867,\\"source\\":\\"/data/input/nginx_public.json\\",\\"offset\\":1020038216,\\"agent\\":\\"Dalvik/1.6.0 (Linux; U; Android 4.2.2; GN9000 Build/JDQ39)\\",\\"request\\":\\"POST mobile.acme.com/mobile/data\\"}",
                "entities": [
                    {
                        "highlight": {
                            "fields": {},
                            "stored": []
                        }
                    }
                ]
            }
        }
    ],
    "aggregations": {
        "FILTER.TS.MAX": {
            "responseType": "numeric",
            "value": 2.6860884E7,
            "numDocs": 26860884
        }
    },
    "schema": {}
}"""
    data = json.loads(raw)
    req = Request(data["request"])
    req.validate()
    res = Response(data)
    res.validate()
