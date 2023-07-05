from django.urls import path

from . import views
app_name='tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/done/', views.done, name='done'),
    path('<int:pk>/undone/', views.undone, name='undone')
]
