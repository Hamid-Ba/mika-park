from rest_framework import serializers

from cooperation import models

class CooperationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CooperationType
        fields = "__all__"

class CooperationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CooperationRequest
        fields = "__all__"