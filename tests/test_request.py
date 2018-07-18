import json
from dashbase.request import Request
from dashbase.response import Response, ClusterOverviewResponse


def test_model():
    raw = """{
    "request": {
        "numResults": 3,
        "tableNames": [],
        "excludeTableNames": [],
        "startTimeInMillis": 0,
        "endTimeInMillis": 0,
        "startGlobalId": 0,
        "endGlobalId": 9223372036854775807,
        "fields": [],
        "aggregations": {
            "ts_hour_count_all": {
                "requestType": "tsa",
                "bucketSize": 59,
                "subRequest": {
                    "requestType": "numeric",
                    "col": "*",
                    "type": "count"
                }
            }
        },
        "useApproximation": false,
        "ctx": "c2aa1018-d7f7-44de-8bca-2f001da55739",
        "fetchSchema": false,
        "timeoutMillis": 2147483647,
        "disableHighlight": false,
        "debugMode": 0
    },
    "totalDocs": 2629794942,
    "numDocs": 35552127,
    "numHits": 35552127,
    "numDocsProcessed": 35552127,
    "numHitsProcessed": 35552127,
    "latencyInMillis": 484,
    "timeProcessedTo": 1531893385,
    "isTimedOut": false,
    "startId": "nginx_json:0%3A5b4ed98a%2C1%3A5b4ed98c",
    "endId": "nginx_json:0%3A5b4ed686%2C1%3A5b4ed688",
    "debugMap": {},
    "hits": [
        {
            "timeInMillis": 1531894156548,
            "globalId": 6579435305248489345,
            "payload": {
                "fields": {},
                "stored": "{\\"@timestamp\\":\\"2018-07-18T06:09:16.548Z\\",\\"source\\":\\"/data/input/nginx_public.json\\",\\"offset\\":7521605024,\\"bytesSent\\":832,\\"response\\":200,\\"host\\":\\"78.99.63.88\\",\\"agent\\":\\"Dalvik/2.1.0 (Linux; U; Android 5.0.2; HTC D816t Build/LRX22G)\\",\\"_subtable\\":\\"producer1\\",\\"beat\\":{\\"name\\":\\"9fd50d6ba7c5\\",\\"hostname\\":\\"9fd50d6ba7c5\\",\\"version\\":\\"6.1.1\\"},\\"request\\":\\"POST mobile.acme.com/mobile/data\\"}",
                "entities": [
                    {
                        "highlight": {
                            "fields": {},
                            "stored": []
                        }
                    }
                ]
            }
        },
        {
            "timeInMillis": 1531894156548,
            "globalId": 6579435305248489217,
            "payload": {
                "fields": {},
                "stored": "{\\"@timestamp\\":\\"2018-07-18T06:09:16.548Z\\",\\"beat\\":{\\"name\\":\\"9fd50d6ba7c5\\",\\"hostname\\":\\"9fd50d6ba7c5\\",\\"version\\":\\"6.1.1\\"},\\"offset\\":7521604843,\\"bytesSent\\":665,\\"agent\\":\\"Dalvik/1.6.0 (Linux; U; Android 4.4.3; XM50h Build/19.1.1.C.0.56)\\",\\"source\\":\\"/data/input/nginx_public.json\\",\\"_subtable\\":\\"producer1\\",\\"request\\":\\"POST mobile.acme.com/mobile/data\\",\\"host\\":\\"65.182.173.23\\",\\"response\\":200}",
                "entities": [
                    {
                        "highlight": {
                            "fields": {},
                            "stored": []
                        }
                    }
                ]
            }
        },
        {
            "timeInMillis": 1531894156548,
            "globalId": 6579435305248489089,
            "payload": {
                "fields": {},
                "stored": "{\\"@timestamp\\":\\"2018-07-18T06:09:16.548Z\\",\\"source\\":\\"/data/input/nginx_public.json\\",\\"request\\":\\"POST mobile.acme.com/mobile/data\\",\\"host\\":\\"238.149.69.208\\",\\"agent\\":\\"Dalvik/1.6.0 (Linux; U; Android 4.2.1; vivo X1S Build/JOP40D)\\",\\"_subtable\\":\\"producer1\\",\\"beat\\":{\\"name\\":\\"9fd50d6ba7c5\\",\\"hostname\\":\\"9fd50d6ba7c5\\",\\"version\\":\\"6.1.1\\"},\\"response\\":200,\\"bytesSent\\":870,\\"offset\\":7521604657}",
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
        "ts_hour_count_all": {
            "responseType": "tsa",
            "bucketSizeInSeconds": 59,
            "buckets": [
                {
                    "timeInSec": 1531893287,
                    "count": 86283,
                    "response": {
                        "responseType": "numeric",
                        "value": 86283.0,
                        "numDocs": 86283
                    }
                },
                {
                    "timeInSec": 1531893346,
                    "count": 2578165,
                    "response": {
                        "responseType": "numeric",
                        "value": 2578165.0,
                        "numDocs": 2578165
                    }
                },
                {
                    "timeInSec": 1531893405,
                    "count": 2624837,
                    "response": {
                        "responseType": "numeric",
                        "value": 2624837.0,
                        "numDocs": 2624837
                    }
                },
                {
                    "timeInSec": 1531893464,
                    "count": 2602203,
                    "response": {
                        "responseType": "numeric",
                        "value": 2602203.0,
                        "numDocs": 2602203
                    }
                },
                {
                    "timeInSec": 1531893523,
                    "count": 2555422,
                    "response": {
                        "responseType": "numeric",
                        "value": 2555422.0,
                        "numDocs": 2555422
                    }
                },
                {
                    "timeInSec": 1531893582,
                    "count": 2574249,
                    "response": {
                        "responseType": "numeric",
                        "value": 2574249.0,
                        "numDocs": 2574249
                    }
                },
                {
                    "timeInSec": 1531893641,
                    "count": 2559728,
                    "response": {
                        "responseType": "numeric",
                        "value": 2559728.0,
                        "numDocs": 2559728
                    }
                },
                {
                    "timeInSec": 1531893700,
                    "count": 2567193,
                    "response": {
                        "responseType": "numeric",
                        "value": 2567193.0,
                        "numDocs": 2567193
                    }
                },
                {
                    "timeInSec": 1531893759,
                    "count": 2579256,
                    "response": {
                        "responseType": "numeric",
                        "value": 2579256.0,
                        "numDocs": 2579256
                    }
                },
                {
                    "timeInSec": 1531893818,
                    "count": 2583768,
                    "response": {
                        "responseType": "numeric",
                        "value": 2583768.0,
                        "numDocs": 2583768
                    }
                },
                {
                    "timeInSec": 1531893877,
                    "count": 2559144,
                    "response": {
                        "responseType": "numeric",
                        "value": 2559144.0,
                        "numDocs": 2559144
                    }
                },
                {
                    "timeInSec": 1531893936,
                    "count": 2622489,
                    "response": {
                        "responseType": "numeric",
                        "value": 2622489.0,
                        "numDocs": 2622489
                    }
                },
                {
                    "timeInSec": 1531893995,
                    "count": 2596126,
                    "response": {
                        "responseType": "numeric",
                        "value": 2596126.0,
                        "numDocs": 2596126
                    }
                },
                {
                    "timeInSec": 1531894054,
                    "count": 2593236,
                    "response": {
                        "responseType": "numeric",
                        "value": 2593236.0,
                        "numDocs": 2593236
                    }
                },
                {
                    "timeInSec": 1531894113,
                    "count": 1870028,
                    "response": {
                        "responseType": "numeric",
                        "value": 1870028.0,
                        "numDocs": 1870028
                    }
                }
            ]
        }
    },
    "schema": {}
}"""
    data = json.loads(raw)
    req = Request(data["request"], strict=True)
    req.validate()
    res = Response(data, strict=True)
    res.validate()


def test_ClusterOverviewResponse():
    raw = """
    {"clusterPrefix":"docker","overview":{"nginx_json":{"metrics":{"system":{"cpuLoadFactor":2.2,"cpuUsagePercent":35.04406009335651,"numCores":8,"heapUsage":8511986456,"heapUsagePercent":49.546282133087516,"diskUsage":4370664448,"diskUsagePercent":0.1379402375132169},"indexing":{"numBytesPerSecond":24170504,"numBytesPerDay":2271156278400,"numEventsPerSecond":33865,"numEventsPerDay":3175804800},"query":{"avgLatencyMillis":0,"minLatencyMillis":0,"maxLatencyMillis":174,"p99LatencyMillis":1,"medianLatencyMillis":0,"queriesPerSecond":0},"isError":false},"info":{"0":["10.0.0.248:7888"],"1":["10.0.0.243:7888"]}}}}
    """
    data = json.loads(raw)
    req = ClusterOverviewResponse(data)
    req.values()


def test_response():
    data = {'request': {'numResults': 10, 'tableNames': [], 'excludeTableNames': [], 'query': {'queryType': 'string', 'queryStr': 'SM-N9106W and 200'}, 'startTimeInMillis': 0, 'endTimeInMillis': 0, 'startGlobalId': 0, 'endGlobalId': 9223372036854775807, 'fields': ['agnet', 'request', 'offset'], 'aggregations': {}, 'useApproximation': False, 'ctx': 'eeb26380-03aa-4977-84b4-b1bfd10de2d1', 'fetchSchema': False, 'timeoutMillis': 2147483647, 'disableHighlight': True, 'debugMode': 0}, 'totalDocs': 2795787809, 'numDocs': 35523977, 'numHits': 10173, 'numDocsProcessed': 2402142, 'numHitsProcessed': 688, 'latencyInMillis': 80, 'timeProcessedTo': 1531910216, 'isTimedOut': False, 'startId': 'nginx_json:0%3A5b4f1b41%2C1%3A5b4f1b44', 'endId': 'nginx_json:0%3A5b4f1844%2C1%3A5b4f1847', 'debugMap': {}, 'hits': [{'timeInMillis': 1531910979742, 'globalId': 6579507563778113281, 'payload': {'fields': {'request': ['POST mobile.acme.com/mobile/data'], 'offset': ['4.679457867E9']}, 'stored': '{"@timestamp":"2018-07-18T10:49:39.742Z","response":200,"offset":4679457867,"_subtable":"producer3","beat":{"version":"6.1.1","name":"6c3064878ef6","hostname":"6c3064878ef6"},"request":"POST mobile.acme.com/mobile/data","host":"67.5.235.16","source":"/data/input/nginx_public.json","bytesSent":913,"agent":"Dalvik/1.6.0 (Linux; U; Android 4.4.4; SM-N9106W Build/KTU84P)"}', 'entities': [{'highlight': {'fields': {}, 'stored': [{'offset': 52, 'length': 3}, {'offset': 346, 'length': 2}, {'offset': 349, 'length': 6}]}}]}}, {'timeInMillis': 1531910979721, 'globalId': 6579507563778036097, 'payload': {'fields': {'request': ['POST mobile.acme.com/mobile/data'], 'offset': ['4.674231256E9']}, 'stored': '{"@timestamp":"2018-07-18T10:49:39.721Z","source":"/data/input/nginx_public.json","host":"132.136.86.11","response":200,"bytesSent":3821,"agent":"Dalvik/2.1.0 (Linux; U; Android 5.0.1; SM-N9106W Build/LRX22C)","offset":4674231256,"_subtable":"producer1","beat":{"name":"d820e5d4f436","hostname":"d820e5d4f436","version":"6.1.1"},"request":"POST mobile.acme.com/mobile/data"}', 'entities': [{'highlight': {'fields': {}, 'stored': [{'offset': 116, 'length': 3}, {'offset': 185, 'length': 2}, {'offset': 188, 'length': 6}]}}]}}, {'timeInMillis': 1531910979506, 'globalId': 6579507563777419393, 'payload': {'fields': {'request': ['POST mobile.acme.com/mobile/data'], 'offset': ['4.678709827E9']}, 'stored': '{"@timestamp":"2018-07-18T10:49:39.506Z","host":"9.115.17.187","beat":{"name":"6c3064878ef6","hostname":"6c3064878ef6","version":"6.1.1"},"source":"/data/input/nginx_public.json","bytesSent":674,"agent":"Dalvik/2.1.0 (Linux; U; Android 5.0.1; SM-N9106W Build/LRX22C)","request":"POST mobile.acme.com/mobile/data","offset":4678709827,"response":200,"_subtable":"producer3"}', 'entities': [{'highlight': {'fields': {}, 'stored': [{'offset': 243, 'length': 2}, {'offset': 246, 'length': 6}, {'offset': 344, 'length': 3}]}}]}}, {'timeInMillis': 1531910979452, 'globalId': 6579507563777219969, 'payload': {'fields': {'request': ['POST mobile.acme.com/mobile/data'], 'offset': ['4.673547933E9']}, 'stored': '{"@timestamp":"2018-07-18T10:49:39.452Z","_subtable":"producer1","host":"9.115.17.187","bytesSent":689,"request":"POST mobile.acme.com/mobile/data","response":200,"agent":"Dalvik/2.1.0 (Linux; U; Android 5.0.1; SM-N9106W Build/LRX22C)","beat":{"name":"d820e5d4f436","hostname":"d820e5d4f436","version":"6.1.1"},"source":"/data/input/nginx_public.json","offset":4673547933}', 'entities': [{'highlight': {'fields': {}, 'stored': [{'offset': 159, 'length': 3}, {'offset': 211, 'length': 2}, {'offset': 214, 'length': 6}]}}]}}, {'timeInMillis': 1531910979361, 'globalId': 6579507563776950785, 'payload': {'fields': {'request': ['POST mobile.acme.com/mobile/data'], 'offset': ['4.672879351E9']}, 'stored': '{"@timestamp":"2018-07-18T10:49:39.361Z","bytesSent":802,"request":"POST mobile.acme.com/mobile/data","agent":"Dalvik/2.1.0 (Linux; U; Android 5.0.1; SM-N9106W Build/LRX22C)","source":"/data/input/nginx_public.json","_subtable":"producer2","beat":{"name":"a5c655a07e3b","hostname":"a5c655a07e3b","version":"6.1.1"},"offset":4672879351,"host":"132.136.86.11","response":200}', 'entities': [{'highlight': {'fields': {}, 'stored': [{'offset': 150, 'length': 2}, {'offset': 153, 'length': 6}, {'offset': 369, 'length': 3}]}}]}}, {'timeInMillis': 1531910979201, 'globalId': 6579507563776460801, 'payload': {'fields': {'request': ['POST mobile.acme.com/mobile/data'], 'offset': ['4.672879351E9']}, 'stored': '{"@timestamp":"2018-07-18T10:49:39.201Z","offset":4672879351,"host":"132.136.86.11","response":200,"bytesSent":802,"agent":"Dalvik/2.1.0 (Linux; U; Android 5.0.1; SM-N9106W Build/LRX22C)","source":"/data/input/nginx_public.json","request":"POST mobile.acme.com/mobile/data","_subtable":"producer1","beat":{"name":"d820e5d4f436","hostname":"d820e5d4f436","version":"6.1.1"}}', 'entities': [{'highlight': {'fields': {}, 'stored': [{'offset': 95, 'length': 3}, {'offset': 163, 'length': 2}, {'offset': 166, 'length': 6}]}}]}}, {'timeInMillis': 1531910979005, 'globalId': 6579507563775947137, 'payload': {'fields': {'request': ['POST mobile.acme.com/mobile/data'], 'offset': ['4.677303932E9']}, 'stored': '{"@timestamp":"2018-07-18T10:49:39.005Z","offset":4677303932,"bytesSent":674,"host":"9.115.17.187","_subtable":"producer3","beat":{"name":"6c3064878ef6","hostname":"6c3064878ef6","version":"6.1.1"},"agent":"Dalvik/2.1.0 (Linux; U; Android 5.0.1; SM-N9106W Build/LRX22C)","request":"POST mobile.acme.com/mobile/data","response":200,"source":"/data/input/nginx_public.json"}', 'entities': [{'highlight': {'fields': {}, 'stored': [{'offset': 246, 'length': 2}, {'offset': 249, 'length': 6}, {'offset': 327, 'length': 3}]}}]}}, {'timeInMillis': 1531910978648, 'globalId': 6579507563774819201, 'payload': {'fields': {'request': ['POST mobile.acme.com/mobile/data'], 'offset': ['4.671192493E9']}, 'stored': '{"@timestamp":"2018-07-18T10:49:38.648Z","source":"/data/input/nginx_public.json","bytesSent":801,"agent":"Dalvik/1.6.0 (Linux; U; Android 4.4.4; SM-N9106W Build/KTU84P)","host":"238.70.191.61","response":200,"_subtable":"producer1","beat":{"name":"d820e5d4f436","hostname":"d820e5d4f436","version":"6.1.1"},"offset":4671192493,"request":"POST mobile.acme.com/mobile/data"}', 'entities': [{'highlight': {'fields': {}, 'stored': [{'offset': 146, 'length': 2}, {'offset': 149, 'length': 6}, {'offset': 205, 'length': 3}]}}]}}, {'timeInMillis': 1531910978647, 'globalId': 6579507563774817409, 'payload': {'fields': {'request': ['POST mobile.acme.com/mobile/data'], 'offset': ['4.671189003E9']}, 'stored': '{"@timestamp":"2018-07-18T10:49:38.647Z","offset":4671189003,"agent":"Dalvik/1.6.0 (Linux; U; Android 4.4.4; SM-N9106W Build/KTU84P)","bytesSent":810,"_subtable":"producer1","request":"POST mobile.acme.com/mobile/data","host":"238.70.191.61","response":200,"source":"/data/input/nginx_public.json","beat":{"hostname":"d820e5d4f436","version":"6.1.1","name":"d820e5d4f436"}}', 'entities': [{'highlight': {'fields': {}, 'stored': [{'offset': 109, 'length': 2}, {'offset': 112, 'length': 6}, {'offset': 253, 'length': 3}]}}]}}, {'timeInMillis': 1531910978589, 'globalId': 6579507563774699521, 'payload': {'fields': {'request': ['POST mobile.acme.com/mobile/data'], 'offset': ['4.676218986E9']}, 'stored': '{"@timestamp":"2018-07-18T10:49:38.589Z","bytesSent":806,"source":"/data/input/nginx_public.json","_subtable":"producer3","beat":{"name":"6c3064878ef6","hostname":"6c3064878ef6","version":"6.1.1"},"response":200,"agent":"Dalvik/1.6.0 (Linux; U; Android 4.4.4; SM-N9106W Build/KTU84P)","request":"POST mobile.acme.com/mobile/data","host":"65.182.173.155","offset":4676218986}', 'entities': [{'highlight': {'fields': {}, 'stored': [{'offset': 208, 'length': 3}, {'offset': 260, 'length': 2}, {'offset': 263, 'length': 6}]}}]}}], 'aggregations': {}, 'schema': {}}
    req = Request(data["request"], strict=True)
    req.validate()
    res = Response(data, strict=True)
    res.validate()
