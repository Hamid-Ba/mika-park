"""
about us serializers
"""
from aboutus import models
from gallery import serializers as gallery_serial

from rest_framework import serializers


class AboutUsSerializer(serializers.ModelSerializer):
    """About Us Serializer"""
    image = gallery_serial.GallerySerializer(many=False)

    class Meta:
        """Meta Class"""

        model = models.AboutUs
        fields = "__all__"


class AboutUsExtensionSerializer(serializers.ModelSerializer):
    """About Us Extension Serializer"""

    class Meta:
        """Meta Class"""

        model = models.AboutUsExtension
        fields = "__all__"
