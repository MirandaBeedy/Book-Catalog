
from django.test import TestCase
from django.urls import reverse

from .models import Publisher, Book


class BookListViewTests(TestCase):
    def setUp(self):
        self.publisher = Publisher.objects.create(
            name="Bloom Books"
        )
        self.book = Book.objects.create(
            title="Things We Never Got Over",
            author="Lucy Score",
            publication_year=2022,
            publisher=self.publisher
        )

    def test_book_list_displays_book(self):
        response = self.client.get(reverse("book_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Things We Never Got Over")
