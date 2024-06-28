"""
    site info serializers
"""
from siteinfo import models
from gallery import serializers as gallery_serial

from rest_framework import serializers


class HomeHeaderSerializer(serializers.ModelSerializer):
    """Home Header Serializer"""

    logo = gallery_serial.GallerySerializer(many=False)
    media = gallery_serial.MediaSerializer(many=False)
    heading_image = gallery_serial.GallerySerializer(many=False)

    class Meta:
        """Meta Class"""

        model = models.HomeHeader
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    """Service Serializer"""

    logo = gallery_serial.GallerySerializer(many=False)

    class Meta:
        """Meta Class"""

        model = models.Service
        fields = "__all__"


class FeatureSerializer(serializers.ModelSerializer):
    """Feature Serializer"""

    logo = gallery_serial.GallerySerializer(many=False)

    class Meta:
        """Meta Class"""

        model = models.Feature
        fields = "__all__"


class FooterSerializer(serializers.ModelSerializer):
    """Footer Serializer"""

    logo = gallery_serial.GallerySerializer(many=False)

    class Meta:
        """Meta Class"""

        model = models.Footer
        fields = "__all__"


class FooterLinkSerializer(serializers.ModelSerializer):
    """Footer Link Serializer"""

    class Meta:
        """Meta Class"""

        model = models.FooterLink
        fields = "__all__"


class CommunicationSerializer(serializers.ModelSerializer):
    """Communication Serializer"""

    logo = gallery_serial.GallerySerializer(many=False)

    class Meta:
        """Meta Class"""

        model = models.Communication
        fields = "__all__"


class CriticSerializer(serializers.ModelSerializer):
    """Critic Serializer"""

    class Meta:
        """Meta Class"""

        model = models.Critic
        fields = "__all__"
