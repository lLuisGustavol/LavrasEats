import unicodedata
from django.db import models

def normalize_text(text):
    text = text.lower()
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')
    text = text.replace('-', ' ').strip()
    return text

class Restaurante(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    categoria = models.CharField(max_length=100)
    nota_media = models.FloatField(default=0.0)
    numero_avaliacoes = models.PositiveIntegerField(default=0)
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)

    class Meta:
        unique_together = ('nome', 'endereco', 'categoria', 'telefone')

    def save(self, *args, **kwargs):
        # Normaliza a categoria antes de salvar
        self.categoria = normalize_text(self.categoria)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome} - {self.endereco} ({self.categoria})"
