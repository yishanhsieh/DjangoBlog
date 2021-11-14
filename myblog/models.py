from django.db import models
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField
from django.utils.text import slugify

# Create your models here.

class Markdown(models.Model):
    name = models.CharField(max_length =10)
    content = MDTextField()

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

STATUS = (
    (0,"Draft"),
    (1,"Publish")

)


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null= True, blank=True)    
    author = models.ForeignKey(User, on_delete =models.CASCADE, null= True, blank=True)
    updated_on =  models.DateTimeField(auto_now =True)
    content = MDTextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    header_image = models.ImageField(default = 'static/assets/img/post-bg.jpg', upload_to="images/")
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    #category = models.CharField(max_length=255, default ='uncategorized')
    category = models.ForeignKey(Category, on_delete = models.CASCADE, default ='uncategorized')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def save(self, *args, **kwargs):
        value =self.slug
        slug =  slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
