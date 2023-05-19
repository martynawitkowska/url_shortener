import pytest

from shortener.models import URL


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


@pytest.fixture
def short_link_db(db):
    return URL.objects.create(url="https://docs.python.org/3/", short_url="Abye5ijCD0")


@pytest.fixture
def original_url():
    return "https://docs.python.org/3/"
