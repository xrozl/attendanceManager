from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path("login", views.Login, name="Login"),
	path("logout", views.Logout, name="Logout")
]