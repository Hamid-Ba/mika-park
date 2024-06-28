from django.urls import path

from contactus import views

app_name = "contact_us"

urlpatterns = [
    path("message/", views.CreateMessageAPI.as_view(), name="send_message"),
    path("addresses/", views.AddressListAPI.as_view(), name="address_list"),
    path("phones/", views.PhoneListAPI.as_view(), name="phone_list"),
    path("emails/", views.EmailListAPI.as_view(), name="email_list"),
    path("map/", views.MapAPI.as_view(), name="map"),
]
