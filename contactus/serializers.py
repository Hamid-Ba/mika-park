"""
contact us serializers
"""
from contactus import models

from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    """Message Serializer"""

    class Meta:
        """Meta Class"""

        model = models.Message
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    """Address Serializer"""

    class Meta:
        """Meta Class"""

        model = models.Address
        fields = "__all__"


class PhoneSerializer(serializers.ModelSerializer):
    """Phone Serializer"""

    class Meta:
        """Meta Class"""

        model = models.Phone
        fields = "__all__"


class EmailSerializer(serializers.ModelSerializer):
    """Email Serializer"""

    class Meta:
        """Meta Class"""

        model = models.Email
        fields = "__all__"


class MapSerializer(serializers.ModelSerializer):
    """Map Serializer"""

    class Meta:
        """Meta Class"""

        model = models.Map
        fields = "__all__"
