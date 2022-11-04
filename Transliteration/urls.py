from django.urls import path
from . import views

urlpatterns = [
    path('', views.Trans, name='Transliteration'),
    path('predict', views.predict, name='predict'),


]