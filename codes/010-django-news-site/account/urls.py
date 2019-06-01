from django.urls import path
from .views import login_view, logout_view

urlpatterns = [
	path('logout/', view=logout_view, name="logout_view"),
	path('', view=login_view, name="login_view"),
]