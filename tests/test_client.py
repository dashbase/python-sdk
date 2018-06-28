import responses
from dashbase.client import Client
import pytest

client = Client("https://dashbase.dev")


@pytest.mark.incremental
@responses.activate
def test_cluster_tables():
    responses.add(responses.GET, 'https://dashbase.dev/v1/cluster/tables',
                  json=["a", "b", "c"], status=200)
    res = client.cluster_info()
    assert len(res), 3
