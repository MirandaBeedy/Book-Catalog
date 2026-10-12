from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
    
class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )
    reviewer_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.reviewer_name} - {self.book.title}"