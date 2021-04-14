from django.contrib import admin
from . models import Post
# Register your models here.
admin.site.register(Post)

def __str__(self):
    return self.title