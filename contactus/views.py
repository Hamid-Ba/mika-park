from rest_framework import generics

from contactus import models, serializers

# Create your views here.


class CreateMessageAPI(generics.CreateAPIView):
    """Create Message View"""

    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer


class AddressListAPI(generics.ListAPIView):
    """Address List View"""

    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer


class PhoneListAPI(generics.ListAPIView):
    """Phone List View"""

    queryset = models.Phone.objects.all()
    serializer_class = serializers.PhoneSerializer


class EmailListAPI(generics.ListAPIView):
    """Email List View"""

    queryset = models.Email.objects.all()
    serializer_class = serializers.EmailSerializer
