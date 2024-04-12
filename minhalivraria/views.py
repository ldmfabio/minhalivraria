from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from minhalivraria.models import Categoria, Editora, Autor, Livro
from minhalivraria.serializers import CategoriaSerializer, EditoraSerializer, AutorSerializer, LivroDetailSerializer, LivroListSerializer, LivroSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return LivroListSerializer
        elif self.action == "retrieve":  # Corrected line with single ==
            return LivroDetailSerializer
        else:
            return LivroSerializer
