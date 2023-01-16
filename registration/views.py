from django.http import HttpResponse
from django.conf import settings
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import login,logout, authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.shortcuts import render,get_object_or_404,redirect
from employee_manager.forms import SignUpForm


from registration.forms import (
    Register_Form,
    Register_Model,    
    )


def accounts_view(request):
    if request.method == 'GET':
        return render(request,'index/accounts.html')
    else:
        name = request.POST.get('name')
        username = request.POST.get('user') 
        password = request.POST.get('password-conf')
        email = request.POST.get('email')

        user = User.objects.filter (username=username).first()

        if user:
            return HttpResponse('Este usuário já existe')
        
        user = User.objects.create_user(name=name, username=username, password=password, email=email)
        user.save()

        return HttpResponse ('Usuário cadastrado com sucesso')

def login_view(request):
    if request.method == 'GET':                                     # Se o metodo de requisição for igual a "GET" (buscar a página pela URL)
        return render(request, ('index/login.html'))              # Retorna uma renderização do template de 'login'
    else:                                                           # Se não
        username = request.POST['username']                     # A variavel 'username' recebe uma requisição 'POST' para buscar o username cadastrado
        password = request.POST['senha']                           # A variavel 'password' recebe uma requisição 'POST' para buscar a senha cadastrado
        user = authenticate(username = username, password = password)  # A variavel 'User' recebe uma autenticação do 'username' e do 'password'
        msg = 'USUÁRIO OU SENHA INVÁLIDOS'                                                       #######################################################################################
        if user is not None:
            login(request,user)                                                    # Se a varival 'User' retorna uma informação 'True' (verdadeira. Ou seja, se existe este usuário com esta senha)
            return redirect('/home/')             # Retorna uma renderização do template 'home'
        else:
            return render(request, 'index/login.html', {'msg':msg})

def logout_template_view(request):
    return render (request,('index/logout.html'))

def logout_view(request):
    logout(request)
    return redirect ('/')

def password_change_view(request):
    if request.method == 'POST':
        form_change = PasswordChangeForm(request.user,request.POST)
        if form_change.is_valid():
            user = form_change.save()
            update_session_auth_hash(request,user)
            return redirect ('/')
    else:
        form_change = PasswordChangeForm(request.user)
    return render(request, 'index/password_change.html', {'form_change':form_change})

def reset_password_view(request):
    return render(request, 'index/reset_password.html')

def about_view(request):
    return render(request,'index/about.html')

@login_required(login_url="/login/")
def home_view(request):
    timedate = timezone.now()
    return render(request,'index/home.html',{'timedate':timedate})

@login_required
def create_register(request):
    form = Register_Form()
    context = {
        'form':form,
    }
    if request.method == 'POST':
        form = Register_Form(request.POST)
        

        if form.is_valid():
            form.save()
            form = Register_Form()
            context2 = {
        'form':form,
        'msg': 'Empregado registrado com sucesso!'
    }
            return render(request,'registers/create_register.html', context2)
        else:
            form = Register_Form()
            return render(request,'registers/create_register.html', context)
       
    return render(request,'registers/create_register.html', context)

@login_required
def read_register(request):
    template = 'registers/read_register.html' #variavel que guarda a URL do template
    objects = Register_Model.objects.all() #traz todos os cadastros de funcionários
    search = request.GET.get('search') #parametro de GET
    
    if search and search.isdigit():#se o search receber um valor e este valor for um digito:
        objects=objects.filter(id=search)#se for digito, ele procura pela matrícula
    elif search:
        objects=objects.filter(nome__icontains=search)#se for string, ele procura pelo nome.
      

    context = {
        'objects':objects,
    }
    return render(request,template,context)

@login_required
def detail_register(request, id):
    dados = Register_Model.objects.get(id=id)
    context = {
        'dados':dados,
    }
    return render(request, 'registers/detail.html', context)

@login_required
def update_register(request,id):
    dados = Register_Model.objects.get(id=id)
    obj = get_object_or_404(Register_Model, id=id)#Busca o objeto dado pelo ID
    form = Register_Form(request.POST or None, instance = obj) #como o objecto como uma instancia ao formulário
    context = {
        'dados':dados,
        'obj':obj,
        'form':form,
        
    }
    if form.is_valid():
        form.save() #Salva o formulário se for válido
        msg = 'Registro atualizado com sucesso!'
        context = {
        'dados':dados,
        'obj':obj,
        'form':form,
        'msg':msg,
    }
        return render(request,'registers/update.html', context)#
    context = {
        'form':form,
        'dados':dados,
    }
    return render(request,'registers/update.html', context) 

@login_required
def delete_register(request,id):
    
    form = get_object_or_404(Register_Model, id=id)#Busca o objeto dado pelo ID
    registro = Register_Model.objects.get(id=id)
    context = {
        'registro':registro,
    }
    if request.method == 'POST':
        form.delete() #deleta o formulário
        return redirect('/read/')#redireciona à mesma página.
    return render(request,'registers/delete.html',context)