from django.db import models

Gender = (('', '----'),
    ('Male','Male'),
    ('Female','Female'),
    )
    
class Profile(models.Model):
    user = models.OneToOneField(user,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=30 , blank=True)
    description = models.TextField(max_length=300,blank=True)
    birthday = models.DataField(blank=True, null=True)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    Gender = models.CharField(max_length=6, choices=Gender, default="")
    phone_number = models.IntegerField(max_length=10 , blank = false)
    Email = models.EmailField(max_length=40 , blank=True)
    number_of_books_read = models.IntegerField()
    points = models.IntegerField()
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    prefered_category= models.TextField(max_length=500 , blank=True)
    

class Book(models.Model):
    title=models.CharField(max_length=30 , blank=True)
    language= models.CharField(max_length=20 , blank=True)
    author = models.CharField(max_length=30, blank=True)
    category =models.CharField(max_length=60, blank=True)
    avaible = models.BooleanField()
    number_of_copies = models.IntegerField(max= 20 , min= 0)
    description = models.TextField(max_length=500 , blank=True)
    image =  models.ImageField(default='default.jpg',upload_to='book_pics')
class Sessions(models.Model):
    picture = models.ImageField(default='default.jpg',upload_to='book_pics')
    guest_name = models.CharField(max_length=50 , blank=True )
    date = models.DataField(blank=True, null=True)
    info_guest = models.TextField(max_length=500 , blank=True)     
    reviews = models.TextField(max_length=500, blank=True) 
    guest_books = models.TextField(max_length=400 , blank=True)
    session_report = models.TextField(max_length=500 ,blank=True) 
class Reviews (models.Model):
    user    = models.ForeignKeyField(user,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    sessions = models.ForeignKey(Sessions, on_delete = models.CASCADE)
    comment = models.TextField(max_length=600 , blank=True)
    stars = models.IntegerField(max = (5) , min = (1))
    
class Challenge (models.Model):
    user    = models.ForeignKeyField(user, blank = True , null=True,on_delete = models.SET_NULL , related_name = 'answered_by')
    book = models.ManyToManyField(Book)
    question = models.TextField(max_length=200, blank=True)
    answer = models.TextField(max_length=600 , blank=True)
    evaluation = models.IntegerField()
class Author(models.Model):
    user = models.ManyToManyField(Book , on_delete=models.CASCADE)
    Sessions = models.ManyToManyField(Sessions, on_delete=models.CASCADE)
    

    


