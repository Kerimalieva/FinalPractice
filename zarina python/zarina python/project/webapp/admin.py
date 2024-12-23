from django.contrib import admin
from webapp.models import CustomUser, PostImage, Post

admin.site.register(CustomUser)
admin.site.register(Post)
admin.site.register(PostImage)

# Register your models here.
