from django.urls import path
from webapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_file/', views.add_selected_file, name='add_file')
]