"""
    site info views
"""
from rest_framework import generics, response, status

from siteinfo import models, serializers


class HomeHeaderAPI(generics.RetrieveAPIView):
    """Home Header View"""

    queryset = models.HomeHeader.objects.all()
    serializer_class = serializers.HomeHeaderSerializer

    def get(self, request, *args, **kwargs):
        if self.queryset.count():
            return response.Response(
                self.serializer_class(instance=self.queryset.last()).data,
                status=status.HTTP_200_OK,
            )

        return response.Response(
            {"message": "داده ای یافت نشد"}, status=status.HTTP_204_NO_CONTENT
        )


class ServiceListAPI(generics.ListAPIView):
    """Service List View"""

    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer


class FeatureListAPI(generics.ListAPIView):
    """Feature List View"""

    queryset = models.Feature.objects.all()
    serializer_class = serializers.FeatureSerializer


class FooterAPI(generics.RetrieveAPIView):
    """Footer View"""

    queryset = models.Footer.objects.all()
    serializer_class = serializers.FooterSerializer

    def get(self, request, *args, **kwargs):
        if self.queryset.count():
            return response.Response(
                self.serializer_class(instance=self.queryset.last()).data,
                status=status.HTTP_200_OK,
            )

        return response.Response(
            {"message": "داده ای یافت نشد"}, status=status.HTTP_204_NO_CONTENT
        )


class FooterLinkListAPI(generics.ListAPIView):
    """FooterLink List View"""

    queryset = models.FooterLink.objects.all()
    serializer_class = serializers.FooterLinkSerializer


class CommunicationListAPI(generics.ListAPIView):
    """Communication List View"""

    queryset = models.Communication.objects.all()
    serializer_class = serializers.CommunicationSerializer

class CreateCriticAPI(generics.CreateAPIView):
    """Create Critic View"""

    queryset = models.Critic.objects.all()
    serializer_class = serializers.CriticSerializer