# lavraseats_backend/recomendacoes/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from restaurantes.models import Restaurante
from avaliacoes.models import Avaliacao
from .utils import gerar_recomendacao

class GerarRecomendacaoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        categoria = request.data.get('categoria')
        prompt_usuario = request.data.get('prompt')

        if not categoria or not prompt_usuario:
            return Response(
                {'erro': 'Categoria e prompt são obrigatórios.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        restaurantes_filtrados = Restaurante.objects.filter(categoria__iexact=categoria)
        if not restaurantes_filtrados.exists():
            return Response(
                {'erro': f'Nenhum restaurante encontrado para a categoria "{categoria}".'},
                status=status.HTTP_404_NOT_FOUND
            )

        ids_restaurantes = [r.id for r in restaurantes_filtrados]
        avaliacoes_relevantes = Avaliacao.objects.filter(restaurante_id__in=ids_restaurantes)

        resultado = gerar_recomendacao(
            prompt_usuario=prompt_usuario,
            restaurantes=restaurantes_filtrados,
            avaliacoes=avaliacoes_relevantes
        )

        if resultado and resultado["id"]:
            restaurante = Restaurante.objects.get(id=resultado["id"])
            
            imagem_url_absoluta = None
            if restaurante.poster:
                imagem_url_absoluta = request.build_absolute_uri(restaurante.poster.url)

            return Response({
                'restaurante_id': restaurante.id,
                'mensagem_explicativa': resultado["mensagem"],
                'nome': restaurante.nome,
                'imagem_url': imagem_url_absoluta 
            }, status=status.HTTP_200_OK)
        elif resultado:
            return Response({
                'restaurante_id': None,
                'mensagem_explicativa': resultado["mensagem"] or "Nenhum restaurante adequado foi encontrado."
            }, status=status.HTTP_200_OK)
        else:
            return Response(
                {'erro': 'Não foi possível gerar uma recomendação. Tente novamente.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR 
            )