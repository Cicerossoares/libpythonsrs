import pytest

from libpythonsrs import api_github
from unittest.mock import Mock


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/98067396?v=4'
    resp_mock.json.return_value = {
        "login": "Cicerossoares", "id": 98067396, "node_id": "U_kgDOBdhjxA",
        "avatar_url":url,
    }
    get_mock = mocker.patch('libpythonsrs.api_github.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = api_github.buscar_avatar('cicerossoares')
    assert url == url


def test_buscar_avatar_integracao():
    url = api_github.buscar_avatar('cicerossoares')
    assert 'https://avatars.githubusercontent.com/u/98067396?v=4' == url