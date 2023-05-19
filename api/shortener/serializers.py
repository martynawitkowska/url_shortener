import shortuuid
from rest_framework import serializers
from . import models


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.URL
        fields = ("short_url",)


class OriginalURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.URL
        fields = ("url",)

    def save(self, **kwargs):
        original_url = self.validated_data.get("url")
        url = models.URL(url=original_url, short_url=shortuuid.uuid(name=original_url))
        url.save()

        return url
