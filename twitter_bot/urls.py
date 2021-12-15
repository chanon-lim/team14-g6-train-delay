from django.urls import path
from .views import index, test_get_request, bot_event_manager

urlpatterns = [
    path('home', index, name="index"),
    path('', bot_event_manager, name="trainbot"),
]