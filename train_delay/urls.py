from django.urls import path
from . import views


app_name = 'train_delay'
urlpatterns = [
    path('', views.index, name="index"),
    path('detail/<str:operator_en>/<str:railway_en>', views.detail, name="detail"),
]