from django.urls import path
from bolsa import views



urlpatterns = [
    path('', views.index),
   path('<int:pessoa_id>/', views.only, name='pessoa')

]