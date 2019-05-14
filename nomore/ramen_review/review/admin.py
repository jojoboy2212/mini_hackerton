from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import Post, Ramen, Comment, Topping, Extra, MyUser
# Register your models here.
admin.site.register(Post)
admin.site.register(Ramen)
admin.site.register(Comment)
admin.site.register(Topping)
admin.site.register(Extra)
admin.site.register(MyUser)
