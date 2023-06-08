from django.shortcuts import render, redirect, HttpResponse
from .models import Book, Publisher


def root(request):
    return redirect("/books")


def books(request):
    context = {
        "books": Book.objects.all(),
        }	
    return render(request, 'books.html', context)


def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Book.objects.create(title=title, desc=description)
        return redirect('/books')
    else:
        return HttpResponse('Method not allowed', status=405)


def this_book(request, id):
    context = {
        "book": Book.objects.get(id=id),
        "authors": Publisher.objects.all(),
        }	
    return render(request, 'book.html', context)


def add_author_book(request):
    if request.method == 'POST':
        author_id = request.POST.get('author_id')
        book_id = request.POST.get('book_id')
        this_book = Book.objects.get(id=book_id)
        this_publisher = Publisher.objects.get(id=author_id)
        this_publisher.books.add(this_book)
        return redirect("books/" + book_id)
    else:
        return HttpResponse('Method not allowed', status=405)


def authors(request):
    context = {
        "authors": Publisher.objects.all(),
        }	
    return render(request, 'authors.html', context)


def add_author(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        notes = request.POST.get('notes')
        Publisher.objects.create(first_name=first_name, last_name=last_name, notes=notes)
        return redirect('/authors')
    else:
        return HttpResponse('Method not allowed', status=405)


def this_author(request, id):
    context = {
        "author": Publisher.objects.get(id=id),
        "books": Book.objects.all(),
        }	
    return render(request, 'author.html', context)


def add_book_author(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        author_id = request.POST.get('author_id')
        this_book = Book.objects.get(id=book_id)
        this_publisher = Publisher.objects.get(id=author_id)
        this_publisher.books.add(this_book)
        return redirect("authors/" + author_id)
    else:
        return HttpResponse('Method not allowed', status=405)
