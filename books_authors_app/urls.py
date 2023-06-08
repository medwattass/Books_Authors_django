from django.urls import path
from . import views


urlpatterns = [
    path('', views.root),
    path('books/', views.books),
    path('add_book', views.add_book),
    path('books/<int:id>/', views.this_book, name='this_book'),
    path('add_author_book', views.add_author_book),
    path('authors/', views.authors),
    path('add_author', views.add_author),
    path('authors/<int:id>/', views.this_author, name='this_author'),
    path('add_book_author', views.add_book_author),
]