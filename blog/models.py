from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name



class Post(models.Model):
    image = models.ImageField(upload_to='media/images')
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True,null=True)

    class Meta:
        db_table = 'posts'

    def __str__(self):
        return self.title



