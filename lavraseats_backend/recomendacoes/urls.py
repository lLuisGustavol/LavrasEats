from django.urls import path
from .views import GerarRecomendacaoView

urlpatterns = [
    path('', GerarRecomendacaoView.as_view(), name='gerar-recomendacao'),
]