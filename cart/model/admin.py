from django.contrib import admin

from cart.models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Cart)