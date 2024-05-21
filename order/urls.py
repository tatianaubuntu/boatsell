from boat.apps import BoatConfig
from django.urls import path

from order.views import OrderCreateView

app_name = BoatConfig.name


urlpatterns = [
    path('create/<int:pk>/', OrderCreateView.as_view(), name='create'),
    ]
