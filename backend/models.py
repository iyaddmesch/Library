from django.db import models
from django.contrib.auth.models import User
import uuid


# choice fields to be later placed in a separate file
# gender
gender = (('', '----'),
('Male', 'Male'),
('Female', 'Female'))

# languages choice
languages = (('', '---------'),
('English', 'English'), 
('Arabic', 'Arabic'), 
('Danish', 'Danish'), 
('German', 'German'), 
('Spanish', 'Spanish'), 
('French', 'French'),  
('Italian', 'Italian'), 
('Japanese', 'Japanese'),  
('Norwegian', 'Norwegian'), 
('Polish', 'Polish'), 
('Portuguese', 'Portuguese'), 
('Romanian', 'Romanian'), 
('Russian', 'Russian'))


class Author(models.Model):
    id        = models.CharField(editable=False, primary_key=True, max_length=35)
    full_name = models.CharField(max_length=30, blank=True)
    birthday  = models.DataField(blank=True, null=True)
    gender    = models.CharField(max_length=6, choices=Gender, default="")
    picture   = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phone     = models.constants(max_length=10, blank = false)
    email     = models.EmailField(max_length=40, blank=True)

    def __str__(self):
        return str(self.full_name)


class Profile(models.Model):
    id          = models.CharField(editable=False, primary_key=True, max_length=35)
    full_name   = models.CharField(max_length=30, blank=True)
    description = models.TextField(max_length=300, blank=True)
    birthday    = models.DataField(blank=True, null=True)
    gender      = models.CharField(max_length=6, choices=Gender, default="")
    phone       = models.CharField(max_length=15, blank=False)
    email       = models.EmailField(max_length=40, blank=True)
    preferences = models.TextField(max_length=500, blank=True)
    picture     = models.ImageField(default='default_profile.jpg', upload_to='profile_pics')
    books_read  = models.IntegerField(default=0)
    score       = models.IntegerField(default=0)
    #relations
    books       = models.ManyToManyField('Book', related_name='books_authors')
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)


class Book(models.Model):
    slug        = models.SlugField()
    isbn        = models.CharField(max_length=30)
    title       = models.CharField(max_length=30, blank=True)
    language    = models.CharField(max_length=80, null=True, choices=languages, default="")
    published   = models.DataField(blank=True, null=True)
    category    = models.CharField(max_length=60, blank=True )
    available   = models.BooleanField(default=False)
    quantity    = models.IntegerField(max=20, min=0)
    description = models.TextField(max_length=500, blank=True)
    picture     = models.ImageField(default='default_book.jpg', upload_to='book_picture')
    #relations
    authors     = models.ManyToManyField(Author, related_name='authors')
    review      = models.ManyToManyField(Review, related_name='book_reviews')

    def __str__(self):
        return ", ".join([str(self.title) + " " + str(self.slug) + " (" + str(self.isbn) +") "])

class Session(models.Model):
    id      = models.CharField(editable=False, primary_key=True, max_length=35)
    date    = models.DataField(blank=True, null=True)
    picture = models.ImageField(default='default_session.jpg', upload_to='book_pics')
    report  = models.TextField(max_length=500, blank=True) 
    #relations
    authors = models.ManyToManyField(Author, related_name='books_authors')
    reviews = models.ManyToManyField(Review, related_name='session_reviews')

    def __str__(self):
        return ", ".join([str(self.id) + " " + " (" + str(self.date) +") "])


class BookReview(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    comment      = models.TextField(max_length=600 , blank=True)
    stars        = models.IntegerField(max=5, min=1)
    #relations
    review_by    = models.ForeignKeyField(User,on_delete=models.CASCADE)
    book         = models.ForeignKeyField(Book,on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_created']


class SessionReview(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    comment      = models.TextField(max_length=600, blank=True)
    stars        = models.IntegerField(max=5, min=1, default=1)
    #relations
    review_by    = models.ForeignKeyField(User, on_delete=models.CASCADE)
    session      = models.ForeignKeyField(Session, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_created']

    
class challenge(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    answered_by  = models.ForeignKeyField(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='answered_by')
    book         = models.ManyToManyField(Book, blank=True, related_name='related_books')
    question     = models.TextField(max_length=200, blank=True)
    answer       = models.TextField(max_length=600, blank=True)
    evaluation   = models.IntegerField()

    class Meta:
        ordering = ['-date_created']
