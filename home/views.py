from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from home.forms import UserForm
from home.models import Cart, Product


def home(request):
    return render(request, 'index.html')


def shop(request):
    product = Product.objects.all()
    return render(request, 'shop.html',{'product':product})


def contactus(request):
    return render(request, 'contactus.html')


def account(request):
    return render(request, 'account.html')


@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def login_user(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username']
                            , password=request.POST['password'])
        if user is None:
            return render(request,
                          'login.html',
                          {'form': AuthenticationForm(),
                           'error': 'Username or password you entered is incorrect.'})
        else:
            login(request, user)
            return redirect('home')
    else:
        return render(request, 'login.html', {'form': AuthenticationForm()})


def cart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
    else:
        cart = []
    if request.method == 'GET':
        return render(request, 'cart.html', {'cart': cart})


def remove_item(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)
    if request.method == 'POST':
        cart_item.delete()
        return redirect('cart')


def increment_item(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)
    if request.method == 'POST':
        cart_item.quantity += 1
        cart_item.save()
        return redirect('cart')


def decrement_item(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)
    if request.method == 'POST':
        if cart_item.quantity > 0:
            cart_item.quantity -= 1
            cart_item.save()
        return redirect('cart')


def signup_user(request):
    if request.method == 'POST':
        # Create a new user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],
                                                password=request.POST['password1'],
                                                email=request.POST['email'],
                                                first_name=request.POST['first_name'],
                                                last_name=request.POST['last_name'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html',
                              {'form': UserCreationForm(), 'error': 'Username has already been taken'})
        else:
            # Password didn't match
            return render(request, 'signup.html', {'form': UserForm(), 'error': 'Passwords did not match'})
    else:
        return render(request, 'signup.html', {'form': UserForm()})

