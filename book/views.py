from django.shortcuts import render, get_object_or_404, redirect, HttpResponse

from config import settings
from .forms import BookForm, UpdateBookForm, SignUp, LoginForm, EmailForm
from .models import Book
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.views.generic import DetailView


@login_required
def books(request):
    books = Book.objects.all()
    users = User.objects.all()
    return render(request, 'book.html', {'books': books, 'users': users})


def user_books(request, username):
    user = get_object_or_404(User, username=username)
    books = Book.objects.filter(created_by=user)
    return render(request, 'user_books.html', {'books': books, 'user': user})


class BookList(DetailView):
    model = Book
    template_name = 'book_details.html'
    context_object_name = 'book'

    def get_object(self):
        print(self.kwargs)
        year = self.kwargs['year']
        month = self.kwargs['month']
        day = self.kwargs['day']
        slug = self.kwargs['slug']

        return get_object_or_404(
            Book,
            status=Book.Status.PUBLISHED,
            slug=slug,
            publish__year=year,
            publish__month=month,
            publish__day=day
        )


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.created_by = request.user
            form.save()
            return redirect('book:books')
    form = BookForm()
    return render(request, 'form.html', {'form': form})


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = UpdateBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book:books')
    form = UpdateBookForm(instance=book)
    return render(request, 'form.html', {'form': form, 'book': book})


def delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book:books')
    return render(request, 'confirm.html', {'book': book})


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


def postdate(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = f"This shared by {cd['name']}"
            # url = request.build_absolute_uri()
            massage = f"This massage sent by {cd['name']} - {cd['email']}'s comment's {cd['comments']}"
            send_mail(subject,
                      massage,
                      settings.EMAIL_HOST_USER, [cd['to']])
            return render(request, 'succes.html')
    else:
        form = EmailForm()
    return render(request, 'emailform.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('book:login')
