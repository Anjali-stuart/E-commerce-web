
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='shop'),
    path('', views.about, name='about'),
]
