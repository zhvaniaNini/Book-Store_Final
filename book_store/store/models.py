from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category
    
class Book(models.Model):
    COVER_TYPE_CHOICES = [
        ('hardback', 'Hardback'),
        ('paperback', 'Paperback'),
        ('special', 'Special'),
    ]
    name = models.CharField(max_length=200)
    page_count = models.IntegerField()
    cover_type = models.CharField(max_length=20, choices=COVER_TYPE_CHOICES, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='media/', blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
    

