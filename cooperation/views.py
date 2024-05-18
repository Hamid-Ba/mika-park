from rest_framework import generics, status

from cooperation import models, serializers

class CooperationTypeListAPI(generics.ListAPIView):
    queryset = models.CooperationType.objects.all()
    serializer_class = serializers.CooperationTypeSerializer

class SendCooperationRequestAPI(generics.CreateAPIView):
    queryset = models.CooperationRequest.objects.all()
    serializer_class = serializers.CooperationRequestSerializer