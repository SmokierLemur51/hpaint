from django.urls import path
from . import views


# rename all views with prefix public-viewname
urlpatterns = [
    path("", views.index, name="public-index"),
    path("about/", views.about, name="public-about"),
    path("contact/", views.contact, name="public-contact"),
    path("contact/new/", views.new_contact, name="public-new_contact"),
    path("testimonials/", views.testimonials, name="public-testimonials"),
    path("services/", views.services, name="public-services"),
    path("services/residential", views.residential, name="public-residential"),
    path("services/commercial", views.commercial, name="public-commercial"),
    path("services/exterior", views.exterior, name="public-exterior"),
]
