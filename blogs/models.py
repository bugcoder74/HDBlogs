from django.db import models
from django.contrib.auth.models import User

# Creating the Ctegory Model
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"  # In django admin - all models are pluralised - so this model was named categorys :-), what we did here is that we named it categories (Grammar Paglu ..)
    
    def __str__(self):
        return self.category_name

STATUS_CHOICES = (
    ("Draft", "Draft"),
    ("Published", "Published")
)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, blank=True) # part of url that identifies a particular page on website - usually it's title itself but just hifen instead of spaces - used to omit static urls and make the url dynmic - it's useful for search engine optimization
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # on deleting the category - all posts related to the category gets deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE) # If user is deleted - all his posts gets deleted, USER IS IMPORTED FROM THE import on second line of this file - learn this concept
    featured_image = models.ImageField(upload_to='uploads/%y/%m/%d') # %y replaced by year, %m by month and %d by date - this is how we create dynamic folders
    short_description = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=2000)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default="Draft")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title