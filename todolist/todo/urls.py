from rest_framework import routers
from django.urls import path, include

from . import views

# router = routers.DefaultRouter()
# router.register(r'', views.TodoViewSet)

urlpatterns = [
    path('add/', views.add, name='add'),
    path('update/', views.update_task, name='update_task'),
    path('', views.show_all, name='show_all'),
]
