from rest_framework import serializers
from . import models

class BranchSerializer(serializers.ModelSerializer):
    """Branch Serializer"""

    class Meta:
        model = models.Agent_Branch
        fields = "__all__"

class AgentSerializer(serializers.ModelSerializer):
    """Agent Serializer"""

    branches = BranchSerializer(many=True)
    
    class Meta:
        model = models.Agent
        fields = "__all__"