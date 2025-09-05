from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# This is a base model that provides common fields and methods for other models.
class BaseModel(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title 

    class  Meta:
        abstract = True
        
    # Calculates the difference in days between the object's date and the current date.
    def diffNowDate(self):
        fmt = '%Y-%m-%d'
        d1 = datetime.strptime(str(self.date.year)+'-'+str(self.date.month)+'-'+str(self.date.day), fmt)
        d2 = datetime.strptime(str(datetime.now().year)+'-'+str(datetime.now().month)+'-'+str(datetime.now().day), fmt)
        # d1 = datetime.strptime(str(self.date.y), fmt)
        return (d2-d1).days
        

# Represents a category for articles.
class Category(BaseModel):
    pass




# Represents an article.
class Article(BaseModel,models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    publisher = models.ForeignKey(User,on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='def.jpg', blank=True)
    visit = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.title}  cerate time : {str(self.date)}'
    
    # Returns a snippet of the article body.
    def snipBody(self):
        return f'{self.body[0:50]} ...'
    
    # Calculates the difference in days between the article's publication date and the current date.
    def diffNowDate(self):
        fmt = '%Y-%m-%d'
        d1 = datetime.strptime(str(self.date.year)+'-'+str(self.date.month)+'-'+str(self.date.day), fmt)
        d2 = datetime.strptime(str(datetime.now().year)+'-'+str(datetime.now().month)+'-'+str(datetime.now().day), fmt)
        # d1 = datetime.strptime(str(self.date.y), fmt)
        return (d2-d1).days
    
    
# Represents a comment on an article.
class Comment(BaseModel,models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return  self.user.username + '-->' + self.title
    
# Represents a user's vote on an article.
class voite_user(models.Model):
    STATUS_CHOICE = [
    ('5', "Excellent"),
    ('4', "Very Good"),
    ('3', "Not Bad"),
    ('2', "Bad"),
    ('1', "Very Bad"),
]
    voite = models.CharField(max_length=1, choices=STATUS_CHOICE, default=5)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    

    
    def __str__(self):
        return  self.user.username + '-->' + self.voite
    
            
            