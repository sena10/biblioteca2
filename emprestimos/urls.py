
from django import views
from django.urls import path
from emprestimos import views


urlpatterns = [
    path('home/', views.homepage,name='home'),
    path('registration/', views.registration,name='registration'),
    path('logout/', views.logout,name='logout'),
    path('login/', views.login_view,name='login'),
    path('listar-livros/', views.listar_livros,name='listar_livros'),

]
#urlpatterns = [
   # path('home/', views.homepage, template_name='home'),
#]

