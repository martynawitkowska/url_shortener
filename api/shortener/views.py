from django.views import generic
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from . import models, serializers


class CreateShortURLAPIView(generics.CreateAPIView):
    queryset = models.URL.objects.all()
    serializer_class = serializers.OriginalURLSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        url = serializer.save()

        short_url = serializers.URLSerializer(instance=url, context={"request": request})

        return Response(data=short_url.data, status=status.HTTP_201_CREATED)


class ShortURLRedirectView(generic.RedirectView):
    def get_redirect_url(self, *args, short_url, **kwargs):
        url = get_object_or_404(models.URL, short_url=short_url)

        return url.url
