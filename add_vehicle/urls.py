from django.urls import path
from . import views
app_name = 'add_vehcile'
urlpatterns = [
    path('', views.index, name='index'),
]
