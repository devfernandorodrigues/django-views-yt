from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("function", views.home),
    path("class", views.HomeView.as_view()),
]
