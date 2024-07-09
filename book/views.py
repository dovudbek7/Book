from django.shortcuts import render,get_object_or_404, redirect,HttpResponse
from .forms import BookForm, UpdateBookForm, SignUp,LoginForm
from .models import Book
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def books(request):
    books = Book.objects.all()
    return render(request, 'book.html', {'books':books})

def book_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_details.html', {'book':book})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book:books')
    form = BookForm()
    return render(request, 'form.html', {'form':form})

def book_update(request,pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = UpdateBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book:books')
    form = UpdateBookForm(instance=book)
    return render(request, 'form.html', {'form':form,'book':book})

def delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book:books')
    return render(request, 'confirm.html', {'book':book})

def signup(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book:login')
    else:
        form = SignUp()
    return render(request, 'signup.html', {'form': form})

def home(request):
    return HttpResponse('<h1>Home Page</h1>')
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('book:books')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('book:login')