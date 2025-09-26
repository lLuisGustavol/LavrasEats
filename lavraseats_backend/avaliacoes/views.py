from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Avaliacao
from .serializers import AvaliacaoSerializer
from .utils import analisar_sentimento
from restaurantes.models import Restaurante
from rest_framework.permissions import IsAuthenticated

class AvaliarRestauranteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            texto = serializer.validated_data['texto']
            restaurante = serializer.validated_data['restaurante']
            usuario = request.user

            if Avaliacao.objects.filter(usuario=usuario, restaurante=restaurante).exists():
                return Response({'erro': 'Usuário já avaliou este restaurante'}, status=status.HTTP_400_BAD_REQUEST)

            sentimento, nota, texto_gerado = analisar_sentimento(texto)

            avaliacao = serializer.save(sentimento=sentimento, nota=nota, sentimento_texto=texto_gerado)

            # Atualiza nota média
            avaliacoes = Avaliacao.objects.filter(restaurante=restaurante)
            media = sum(a.nota for a in avaliacoes) / avaliacoes.count()
            restaurante.nota_media = round(media, 2)
            restaurante.numero_avaliacoes = avaliacoes.count()
            restaurante.save()

            return Response(AvaliacaoSerializer(avaliacao).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class ListaAvaliacoesView(ListAPIView):
    queryset = Avaliacao.objects.all().order_by('-criado_em')
    serializer_class = AvaliacaoSerializer
    permission_classes = [IsAuthenticated]


class ConsultarAvaliacaoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, restaurante_id):
        usuario = request.user
        try:
            avaliacao = Avaliacao.objects.get(usuario=usuario, restaurante_id=restaurante_id)
            serializer = AvaliacaoSerializer(avaliacao)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Avaliacao.DoesNotExist:
            return Response({'detail': 'Avaliação não encontrada'}, status=status.HTTP_404_NOT_FOUND)


class ListaAvaliacoesUsuarioView(ListAPIView):
    serializer_class = AvaliacaoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        usuario = self.request.user
        return Avaliacao.objects.filter(usuario=usuario).order_by('-criado_em')