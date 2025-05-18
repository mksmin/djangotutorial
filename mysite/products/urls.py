from django.urls import include, path

from .views import index_view

app_name = "products"

urlpatterns = [
    path("", index_view, name="index"),
]
