from django.urls import path  #to link urls path
from . import views #from current directory import views

urlpatterns = {
    path("", views.index, name = "index"),  #index is a def in view
    path("brian", views.brian, name = "brian"),
    path("rachel", views.rachel, name = "rachel"),
    path("<str:name>", views.greet, name="greet")
}