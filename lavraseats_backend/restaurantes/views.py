from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import Restaurante
from .serializers import RestauranteSerializer
import unicodedata

class CadastrarRestauranteView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        serializer = RestauranteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensagem': 'Restaurante cadastrado com sucesso'}, status=201)
        return Response(serializer.errors, status=400)
class ListarRestaurantesView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        restaurantes = Restaurante.objects.all()
        serializer = RestauranteSerializer(restaurantes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ConsultarRestauranteView(APIView):
    def get(self, request, restaurante_id):
        try:
            restaurante = Restaurante.objects.get(id=restaurante_id)
            serializer = RestauranteSerializer(restaurante)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Restaurante.DoesNotExist:
            return Response({'erro': 'Restaurante não encontrado'}, status=status.HTTP_404_NOT_FOUND)

class AtualizarRestauranteView(APIView):
    def put(self, request, restaurante_id):
        try:
            restaurante = Restaurante.objects.get(id=restaurante_id)
        except Restaurante.DoesNotExist:
            return Response({'erro': 'Restaurante não encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = RestauranteSerializer(restaurante, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensagem': 'Restaurante atualizado com sucesso'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeletarRestauranteView(APIView):
    def delete(self, request, restaurante_id):
        try:
            restaurante = Restaurante.objects.get(id=restaurante_id)
            restaurante.delete()
            return Response({'mensagem': 'Restaurante deletado com sucesso'}, status=status.HTTP_200_OK)
        except Restaurante.DoesNotExist:
            return Response({'erro': 'Restaurante não encontrado'}, status=status.HTTP_404_NOT_FOUND)

class RankingRestaurantesView(APIView):
    def get(self, request):
        ordem = request.query_params.get('ordem', 'melhores')

        if ordem == 'piores':
            restaurantes = (Restaurante.objects
                      .filter(numero_avaliacoes__gt=0)
                      .order_by('nota_media', '-numero_avaliacoes')[:10])
        else:  # padrão: melhores
            restaurantes = (Restaurante.objects
                      .filter(numero_avaliacoes__gt=0)
                      .order_by('-nota_media', '-numero_avaliacoes')[:10])

        serializer = RestauranteSerializer(restaurantes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
def normalize_text(text):
    text = text.lower()
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')
    text = text.replace('-', ' ').strip()
    return text

class FiltrarRestaurantesView(APIView):
    def get(self, request):
        categoria = request.query_params.get('categoria', None)
        ordem_nota = request.query_params.get('ordem_nota', None)

        filtros = {}

        if categoria:
            filtros['categoria__iexact'] = categoria.strip()

        restaurantes = Restaurante.objects.filter(**filtros)

        if ordem_nota == 'asc':
            restaurantes = restaurantes.order_by('nota_media')
        elif ordem_nota == 'desc':
            restaurantes = restaurantes.order_by('-nota_media')

        serializer = RestauranteSerializer(restaurantes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)