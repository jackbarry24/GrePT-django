from django.urls import path
from webapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_file/', views.add_selected_file, name='add_file'),
    path('new_message/', views.new_message, name='new_message')
]