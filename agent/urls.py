from django.urls import path

from agent import views

app_name = "agent"

urlpatterns = [
    path("agent/", views.AgentAPI.as_view(), name="agent"),
]