from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name="Author Name")
    email = models.EmailField(unique=True)
    active = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_logged_in = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ":" + self.email

    
     # function for get_absolute_url

    def get_absolute_url(self):
        return reverse('post_by_author', args=[self.pk, self.name])
    
    


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    # function for get_absolute_url

    def get_absolute_url(self):
        return reverse('post_by_category', args=[self.slug])
    
    


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    
     # function for get_absolute_url

    def get_absolute_url(self):
        return reverse('post_by_tag', args=[self.slug])
    
    

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="Slug will be generated automatically from the title")
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


    # function for get_absolute_url

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.pk, self.slug])
    

class Feedback(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Feedback"

    def __str__(self):
        return self.name + "-" + self.email

