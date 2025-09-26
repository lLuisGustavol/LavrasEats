from rest_framework import serializers
from .models import Restaurante

CATEGORIA_FORMATADA = {
    "acai": "Açaí",
    "arabe": "Comida Árabe",
    "cafeteria": "Cafeteria",
    "chinesa": "Comida Chinesa",
    "churrascaria": "Churrascaria",
    "doces": "Doces/Sobremesas",
    "hamburgueria": "Hamburgueria",
    "italiana": "Comida Italiana",
    "japonesa": "Comida Japonesa",
    "marinhos": "Frutos do Mar",
    "marmitex": "Marmitex",
    "mexicana": "Comida Mexicana",
    "nordestina": "Comida Nordestina",
    "pizza": "Pizzaria",
    "porcoes": "Porções",
    "saudavel": "Saudável",
    "sorveteria": "Sorveteria",
    "tapioca": "Tapioca",
    "vegana": "Vegana",
    "vegetariana": "Vegetariana"
}

class RestauranteSerializer(serializers.ModelSerializer):
    poster = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Restaurante
        fields = '__all__'
        read_only_fields = ['nota_media', 'numero_avaliacoes']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if ret.get('poster'):
            ret['poster'] = ret['poster'].split('/')[-1]
        categoria_raw = ret.get('categoria', '').lower()
        ret['categoria'] = CATEGORIA_FORMATADA.get(categoria_raw, categoria_raw.title())
        return ret
