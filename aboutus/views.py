from rest_framework import generics, response, status

from aboutus import models, serializers


class AboutUsAPI(generics.RetrieveAPIView):
    """About Us View"""

    queryset = models.AboutUs.objects.all()
    serializer_class = serializers.AboutUsSerializer

    def get(self, request, *args, **kwargs):
        if self.queryset.count():
            return response.Response(
                self.serializer_class(instance=self.queryset.last()).data,
                status=status.HTTP_200_OK,
            )

        return response.Response(
            {"message": "داده ای یافت نشد"}, status=status.HTTP_204_NO_CONTENT
        )


class AboutUsExtensionListAPI(generics.ListAPIView):
    """About Us Extension List View"""

    queryset = models.AboutUsExtension.objects.all()
    serializer_class = serializers.AboutUsExtensionSerializer
