
from django.urls import path, re_path

from .views import home_view, post_detail, sample_api, about_view

urlpatterns = [
    path('api/', view=sample_api, name="sample_api"),
    #re_path(r'^/(?P<slug>[\w-]+)/$', view=post_detail, name="post_detail"),
    path('about/', view=about_view, name="about_view"),
    path('<slug>/', view=post_detail, name="post_detail"),
    path('', view=home_view, name="home_view"),
]