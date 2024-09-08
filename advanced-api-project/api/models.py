from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

#The Author model is created to be associated with multiple books and each Book is linked to an Author through a foreign key, establishing a one-to-many relationship.