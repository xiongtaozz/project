from django.contrib import admin
from blog.models import *

admin.site.register(User)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
