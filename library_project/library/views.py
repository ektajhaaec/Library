from datetime import date
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from library.forms import RegistrationForm, LoginForm
from library.models import Book, Author, Genre


def books_by_author(request, author_id):
    books = Book.objects.filter(author_id =author_id)
    return render(request,'book_of_genre.html',{'books':books})

def authors_of_genre(request,genre_id):
    authors =Author.objects.filter(genre_id =genre_id)
    return render(request,'authors_of_genre.html',{'anthors':authors})

def add_book(request):
    author = Author.objects.create(name='Author Name',birth_date=date(1990, 1, 1), nationality= 'Nationality')
    genre = Genre.objects.create(name='Genre Name')
    new_book = Book.objects.create(title ='Book Title',author =author, publication_date= date(2022, 1, 1), price=19.90)
    new_book.genre.add(genre)
    return HttpResponse('New book added successfully!')

def update_book(request, book_id):
    book_to_update =Book.objects.get(pk=book_id)
    new_price =24.99
    book_to_update.price=new_price
    book_to_update.save()
    return HttpResponse('Book updated successfully!')

def remove_genre_from_book(request, book_id, genre_id):
    book_to_update = Book.objects.get(pk=book_id)
    book_to_update = get_object_or_404(Book,pk=book_id)
    genre_to_remove = Book.objects.get(pk= genre_id)
    #genre_to_remove = get_object_or_404(Genre,name= genre_name)
    book_to_update.genre.remove(genre_to_remove)
    book = Book.objects.get(pk=book_id)
   # return HttpResponse(request,'Genre removed from book successfully!')

    return render(request, 'book_detail.html', {'book': book})


def book_detail_view(request, book_id):
    # Retrieve the book object
    book = Book.objects.get(pk=book_id)
    return render(request, 'book_detail.html', {'book': book})

def author_detail_view(request, author_id):
    # Retrieve the author object
    author = Author.objects.get(pk=author_id)
    return render(request, 'author_detail.html', {'author': author})

def genre_list_view(request):
    # Retrieve all genres
    genres = Genre.objects.all()
    return render(request, 'genre_list.html', {'genres': genres})

def home_view(request):
    books =Book.objects.all()
    return render(request, 'home.html',{'books':books})
@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
            else:
                user = User.objects.create_user(username=username, password=password)
                messages.success(request, 'Account created successfully. Please login.')
                return redirect('user_login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
@csrf_exempt
@login_required
def protected_view(request):
    return JsonResponse({'message':'This is a protected view.Only authenticated users can access it.'})
@login_required()
def user_logout(request):
    logout(request)
    return redirect('home')







