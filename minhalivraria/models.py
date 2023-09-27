from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name_plural = 'Categorias'
        verbose_name = 'Categoria'
    

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = 'Editoras'
        verbose_name = 'Editora'
    

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = 'Autores'
        verbose_name = 'Autor'


class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    quantidade = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='livros')
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name='livros')

    def __str__(self) -> str:
        return f"{self.titulo} ({self.quantidade})"
    
    class Meta:
        verbose_name_plural = 'Livros'
        verbose_name = 'Livro'
        ordering = ['titulo']