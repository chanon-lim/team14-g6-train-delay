from django.urls import path
from . import views


app_name = 'train_delay'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>/detail', views.detail, name="detail"),
]