"""
Blog Module Views
"""
from django.utils import timezone
from rest_framework import generics, filters

from config import pagination
from new import serializers, models


class NewDetailView(generics.RetrieveAPIView):
    """Detail Of New View"""

    lookup_field = "slug"
    queryset = models.New.objects.all()
    serializer_class = serializers.NewSerializer


class NewsView(generics.ListAPIView):
    """List Of News View"""

    queryset = models.New.objects.all()
    pagination_class = pagination.StandardPagination
    serializer_class = serializers.NewSerializer

    def get_queryset(self):
        return self.queryset.filter(publish_date__lte=timezone.now()).order_by(
            "-publish_date"
        )


class LatestNewView(generics.ListAPIView):
    """List Of Latest New View"""

    queryset = models.New.objects.order_by("-publish_date")
    serializer_class = serializers.LatestNewSerializer

    def get_queryset(self):
        return self.queryset.filter(publish_date__lte=timezone.now())[:3]


class SearchNewsAPI(generics.ListAPIView):
    """Search News API"""

    queryset = models.New.objects.all()
    serializer_class = serializers.NewSerializer
    pagination_class = pagination.StandardPagination
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    ordering_fields = ["publish_date"]
    search_fields = ["title", "slug", "short_desc"]

    def get_queryset(self):
        return self.queryset.filter(publish_date__lte=timezone.now()).order_by(
            "-publish_date"
        )
