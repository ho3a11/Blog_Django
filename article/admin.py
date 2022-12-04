from django.contrib import admin
from . models import Article,Category,Comment,voite_user

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(voite_user)
