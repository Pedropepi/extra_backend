from django.urls import path
from .views import listar_disciplinas


urlpatterns = [
path('disciplinas/', listar_disciplinas),]