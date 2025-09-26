from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (CadastrarRestauranteView, ListarRestaurantesView, ConsultarRestauranteView, AtualizarRestauranteView,
                     DeletarRestauranteView, RankingRestaurantesView, FiltrarRestaurantesView)

urlpatterns = [
    path('cadastrar/', CadastrarRestauranteView.as_view(), name='cadastrar-restaurante'),
    path('listar/', ListarRestaurantesView.as_view(), name='listar-restaurantes'),
    path('consultar/<int:restaurante_id>', ConsultarRestauranteView.as_view(), name='consultar-restaurante'),
    path('atualizar/<int:restaurante_id>', AtualizarRestauranteView.as_view(), name='atualizar-restaurante'),
    path('deletar/<int:restaurante_id>', DeletarRestauranteView.as_view(), name='deletar-restaurante'),
    path('ranking/', RankingRestaurantesView.as_view(), name='ranking-restaurantes'),
    path('filtrar/', FiltrarRestaurantesView.as_view(), name='filtrar-restaurantes'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
