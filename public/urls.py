from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, "index"),
    path("services/", views.services, "services"),
]