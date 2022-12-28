from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return  self.full_name()
    
class Tag(models.Model):
    caption = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.caption }"
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=1500)
    image_name = models.CharField(max_length=15)
    author = models.ForeignKey(Author,null=True, on_delete=models.SET_NULL, related_name="posts")
    slug = models.SlugField(unique=True)
    tag = models.ManyToManyField(Tag,)
    date = models.DateField(auto_now=True)
    content = models.TextField(validators=[MinLengthValidator(10)],blank=True)
    
    
    
    

    
