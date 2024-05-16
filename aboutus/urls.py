from django.urls import path

from aboutus import views

app_name = "about_us"

urlpatterns = [
    path("about_us/", views.AboutUsAPI.as_view(), name="about_us"),
    path("extensions/", views.AboutUsExtensionListAPI.as_view(), name="extension_list"),
]
