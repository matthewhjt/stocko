from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from main.forms import ProductForm
from main.models import Product
from django.urls import reverse
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages  
import datetime

@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'nama': request.user.username,
        'kelas': 'PBP C',
        'products': products,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

@login_required(login_url='/login')
def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login')
def show_xml_by_id(request, id):
    data = Product.objects.filter(user=request.user, pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

@login_required(login_url='/login')
def show_json_by_id(request, id):
    data = Product.objects.filter(user=request.user, pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login')
def show_html(request):
    data = Product.objects.filter(user=request.user)
    
    context = {
        'products': data,
    }

    return render(request, "show_product.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def add_amount(request, id):
    product = Product.objects.get(user=request.user, pk=id)
    product.add_amount()
    product.save()
    return HttpResponseRedirect(reverse('main:show_main'))

@login_required(login_url='/login')
def subtract_amount(request, id):
    product = Product.objects.get(user=request.user, pk=id)
    product.subtract_amount()
    product.save()
    return HttpResponseRedirect(reverse('main:show_main'))

@login_required(login_url='/login')
def delete_product(request, id):
    product = Product.objects.get(user=request.user, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))