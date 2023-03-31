from django.db import models
from django.contrib.auth.models import User




class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    editora = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('disponivel', 'Disponível'), ('emprestado', 'Emprestado'), ('manutencao', 'Em manutenção')])
    imagem = models.ImageField(upload_to='livros/', null=True, blank=True)
    data_cadastro = models.DateField(auto_now_add=True)
    autor = models.CharField(max_length=200)
    
    def __str__(self):
        return self.titulo

    

class Emprestimo(models.Model):
    codigo = models.CharField(max_length=10)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.codigo} - {self.livro.titulo} ({self.usuario.username})"



class Autor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    data_cadastro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome



class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')

    def __str__(self):
        return self.usuario.username


