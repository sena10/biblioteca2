from django import forms
from .models import Livro, Emprestimo, Autor, Perfil

class LivrosForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'descricao', 'editora', 'status', 'imagem', 'autor']
       

        

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['codigo', 'usuario', 'livro','data_devolucao']
        

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'email']

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nome', 'email', 'avatar']
