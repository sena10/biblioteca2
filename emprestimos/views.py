from imaplib import _Authenticator
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Livro, Emprestimo, Autor, Perfil
from .forms import LivrosForm, EmprestimoForm, MyUserCreationForm
from django.contrib.auth import logout as user_logout


def homepage(request):
    
    return render(request, 'main/home.html')

def registration(request):
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = MyUserCreationForm()
            return render(request, "main/home.html", {'form': form})
    else:
        form = MyUserCreationForm()
        return render(request, "main/registration.html", {'form': form})
    
def logout(request):
    user_logout(request)
    return redirect('home')

def login_view(request):
    if request.method == 'GET':
      return render(request, template_name='main/login.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Tratar o erro de autenticação aqui
            return render(request, 'login', {'error_message': 'Nome de usuário ou senha inválido.'})
    else:
        return render(request, 'home')
        

def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'main/listar-livros.html', {'livros': livros})
    





#def homepage(request):
    #return render(request, template_name='emprestimos/home.html')


#def livro_detalhe(request, pk):
   # livro = get_object_or_404(Livro, pk=pk)
   # emprestimo_form = EmprestimoForm(request.POST or None, initial={'livro': livro})
  #  if request.user.is_authenticated:
       # if emprestimo_form.is_valid():
       ##     emprestimo = emprestimo_form.save(commit=False)
      #      emprestimo.usuario = request.user
       #     emprestimo.save()
        #    messages.success(request, f'O livro {livro.titulo} foi emprestado para você.')
       #     return redirect('home')
 #   return render(request, 'livro_detalhe.html', {'livro': livro, 'emprestimo_form': emprestimo_form})
