from django.test import RequestFactory

from shortener.models import URL
from shortener.serializers import OriginalURLSerializer, URLSerializer


def test_original_url_serializer_valid_serializer(original_url):
    serializer = OriginalURLSerializer(data={"url": original_url})

    assert serializer.is_valid()


def test_original_url_serializer_saves_vaild_url(original_url, db):
    serializer = OriginalURLSerializer(data={"url": original_url})
    serializer.is_valid(raise_exception=True)
    url = serializer.save()

    assert isinstance(url, URL)
    assert url.url == original_url


def test_url_serializer_builds_absolute_uri(short_link_db):
    factory = RequestFactory()
    request = factory.get(f"/{short_link_db.short_url}/")

    serializer = URLSerializer(instance=short_link_db, context={"request": request})

    short_url = serializer.data["short_url"]
    expected_url = request.build_absolute_uri("/") + short_link_db.short_url

    assert short_url == expected_url
