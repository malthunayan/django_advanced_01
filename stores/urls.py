from django.urls import path
from .views import store_list

app_name = 'stores'

urlpatterns = [
    path('list/', store_list, name='list'),
]

