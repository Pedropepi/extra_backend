from django.urls import path
from .views import listar_avaliacoes


urlpatterns = [
path('avaliacoes/', listar_avaliacoes),]