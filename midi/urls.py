from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='midi.index'),
    path('midi/<int:pk>/', views.view, name='midi.view'),
]
