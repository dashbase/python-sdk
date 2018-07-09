from dashbase.client import Client
import os

client = Client("https://staging.dashbase.io:9876", token=os.environ["DASHBASE_TEST_TOKEN"])


def test_get_all_tables():
    res = client.all_cluster_info()
    print(res)


def test_cluster_tables():
    res = client.info()
    print(res)
    res = client.info(names=["nginx_json"])
    print(res)
    res = client.info(names=["wtf"])
    print(res)
