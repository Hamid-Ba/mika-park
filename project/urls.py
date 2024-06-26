from rest_framework.routers import DefaultRouter
from django.urls import path, include

from project import views

app_name = "project"

router = DefaultRouter()
router.register("projects", views.ProjectViewSet)
router.register("blocks", views.BlockViewSet)


urlpatterns = [path("", include(router.urls))]
