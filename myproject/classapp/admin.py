from django.contrib import admin
from . models import Info
from . models import Thread
from . models import Post

# Register your models here.
admin.site.register(Info)
admin.site.register(Thread)
admin.site.register(Post)