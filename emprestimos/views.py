from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Livro, Emprestimo, Autor, Perfil
from .forms import LivrosForm, EmprestimoForm



def homepage(request):
    
    livros = Livro.objects.all()
    return render(request, 'main/home.html', {'livros': livros})





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
