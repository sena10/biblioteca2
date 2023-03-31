
from django import views
from django.urls import path
from emprestimos import views


urlpatterns = [
    path('home/', views.homepage,name='home'),

]
#urlpatterns = [
   # path('home/', views.homepage, template_name='home'),
#]

