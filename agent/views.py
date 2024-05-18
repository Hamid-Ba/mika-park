from rest_framework import generics, response, status

from agent import models, serializers

class AgentAPI(generics.RetrieveAPIView):
    queryset = models.Agent.objects.all()
    serializer_class = serializers.AgentSerializer
    
    def get(self, request, *args, **kwargs):
        if self.queryset.count():
            return response.Response(
                self.serializer_class(instance=self.queryset.last()).data,
                status=status.HTTP_200_OK,
            )

        return response.Response(
            {"message": "داده ای یافت نشد"}, status=status.HTTP_204_NO_CONTENT
        )