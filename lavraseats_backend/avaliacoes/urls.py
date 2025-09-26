from django.urls import path
from .views import AvaliarRestauranteView, ListaAvaliacoesView, ConsultarAvaliacaoView, ListaAvaliacoesUsuarioView

urlpatterns = [
    path('avaliar/', AvaliarRestauranteView.as_view(), name='avaliar-restaurante'),
    path('listar/', ListaAvaliacoesView.as_view(), name='listar-avaliacoes'),
    path('consultar/<int:restaurante_id>/', ConsultarAvaliacaoView.as_view(), name='consultar-avaliacao'),
    path('minhas-avaliacoes/', ListaAvaliacoesUsuarioView.as_view(), name='lista-avaliacoes-usuario'),

]
