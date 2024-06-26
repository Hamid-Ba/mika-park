"""
New Module Serializer
"""
from rest_framework import serializers

from new import models
from gallery import serializers as gallery_serializers


class NewSerializer(serializers.ModelSerializer):
    """New Serializer"""

    image = gallery_serializers.GallerySerializer(many=False)

    class Meta:
        model = models.New
        fields = "__all__"


class LatestNewSerializer(serializers.ModelSerializer):
    """Latest New Serializer"""

    image = gallery_serializers.GallerySerializer(many=False)

    class Meta:
        model = models.New
        fields = ["title", "slug", "short_desc", "publish_date", "image"]


class NewsletterMemberSerializer(serializers.ModelSerializer):
    """Newsletter Member Serializer"""

    class Meta:
        model = models.NewsletterMember
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    """Comment Serializer"""

    class Meta:
        model = models.Comment
        fields = "__all__"
