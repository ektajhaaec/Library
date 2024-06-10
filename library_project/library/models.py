from django.db import models

class Author(models.Model):
    objects = None
    name =models.CharField(max_length =100)
    birth_date =models.DateField()
    nationality =models.CharField(max_length =30)
    def __str__(self):
        return self.name

class Genre(models.Model):
    objects = None
    name =models.CharField(max_length =100)
    def __str__(self):
        return self.name

class Book(models.Model):
    objects = None
    title =models.CharField(max_length=100)
    author=models.ForeignKey(Author,on_delete =models.CASCADE)#In this case, CASCADE means that if an Author object is deleted, all associated Book objects will also be deleted.
    genre=models.ManyToManyField(Genre)
    price =models.DecimalField(max_digits=10,decimal_places =2)
    publication_date=models.DateField()
    def __str__(self):
        return self.title

