from rest_framework import routers
from django.urls import path, include

from . import views

# router = routers.DefaultRouter()
# router.register(r'', views.TodoViewSet)

urlpatterns = [
    path('add/', views.add, name='add'),
    path('update/', views.update_task, name='update_task'),
    path('delete/<str:id>/', views.delete, name='delete'),
    path('clear/', views.clear, name='clear'),
    path('sortbydeadline/', views.show_by_deadline, name='show_by_deadline'),
    path('sortbydatecreated/', views.show_by_created_at, name='show_by_created_at'),
    path('', views.show_all, name='show_all'),
]
