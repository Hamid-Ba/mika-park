from django.urls import path

from siteinfo import views

app_name = "site_info"

urlpatterns = [
    path("header/", views.HomeHeaderAPI.as_view(), name="header"),
    path("services/", views.ServiceListAPI.as_view(), name="service_list"),
    path("features/", views.FeatureListAPI.as_view(), name="feature_list"),
    path("footer/", views.FooterAPI.as_view(), name="footer"),
    path("footer_links/", views.FooterLinkListAPI.as_view(), name="footer_link_list"),
    path(
        "communications/",
        views.CommunicationListAPI.as_view(),
        name="communication_list",
    ),
    path("critic/", views.CreateCriticAPI.as_view(), name="send_critic"),
]
