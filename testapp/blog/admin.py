from django.contrib import admin
from blog import models

class DocumentAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Location, DocumentAdmin)
admin.site.register(models.Job, CommentAdmin)
