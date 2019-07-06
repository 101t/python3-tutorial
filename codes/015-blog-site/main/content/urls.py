from django.urls import path

from .views import home_view, contact_view, about_view, article_detail

urlpatterns = [
    path("about/", view=about_view, name="about_view"),
    path("contact/", view=contact_view, name="contact_view"),
    path("<str:slug>/", view=article_detail, name="article_detail"),
    path("", view=home_view, name="home_view"),
]