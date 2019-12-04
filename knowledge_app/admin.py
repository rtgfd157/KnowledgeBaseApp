from django.contrib import admin

from knowledge_app.models import Subject, Url_Link, Comment

admin.site.register(Subject)
admin.site.register(Url_Link)
admin.site.register(Comment)