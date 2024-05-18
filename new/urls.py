from rest_framework.routers import DefaultRouter
from django.urls import (
    path,
    include,
)

from new import views


router = DefaultRouter()

app_name = "new"

urlpatterns = [
    path("", include(router.urls)),
    path("<str:slug>/", views.NewDetailView.as_view(), name="new_detail"),
    path("news", views.NewsView.as_view(), name="news-list"),
    path("search_news", views.SearchNewsAPI.as_view(), name="search_news"),
    path("latest-news-list", views.LatestNewView.as_view(), name="latest-news-list"),
    path(
        "send_request",
        views.SendNewsletterRequestAPI.as_view(),
        name="send_newsletter_request",
    ),
]
