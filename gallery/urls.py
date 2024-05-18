from django.urls import path

from gallery import views

app_name = "gallery"

urlpatterns = [
    path("galleries/", views.GalleryList.as_view(), name="gallery_list"),
]
