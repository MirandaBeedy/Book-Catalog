
from django.views.generic import ListView
from .models import Book, Publisher, Review


class BookListView(ListView):
    model = Book
    template_name = "catalog/book_list.html"
    context_object_name = "books"
    

class PublisherListView(ListView):
    model = Publisher
    template_name = "catalog/publisher_list.html"
    context_object_name = "publishers"


class ReviewListView(ListView):
    model = Review
    template_name = "catalog/review_list.html"
    context_object_name = "reviews"
