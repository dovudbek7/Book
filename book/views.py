from django.shortcuts import render,get_object_or_404, redirect
from .forms import BookForm,UpdateBookForm
from .models import Book

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