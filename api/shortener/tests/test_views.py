from rest_framework import status
from rest_framework.reverse import reverse

from shortener.models import URL


def test_create_short_url(api_client, db):
    url = "/api/v1/urls/"
    data = {"url": "https://docs.python.org/3/"}

    response = api_client.post(url, data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert URL.objects.count() == 1
    assert URL.objects.first().url == "https://docs.python.org/3/"


def test_short_url_redirect(api_client, short_link_db):
    redirect_url = reverse("shortener:redirect", kwargs={"short_url": short_link_db.short_url})

    response = api_client.get(redirect_url)

    assert response.status_code == status.HTTP_302_FOUND
    assert response.url == short_link_db.url
