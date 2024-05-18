from django.urls import path

from cooperation import views

app_name = "cooperation"

urlpatterns = [
    path(
        "types/", views.CooperationTypeListAPI.as_view(), name="cooperation_type_list"
    ),
    path(
        "send_request/",
        views.SendCooperationRequestAPI.as_view(),
        name="cooperation_request",
    ),
]
