from django.contrib import admin

from .models import Proyecto, Testimonio, Crecimiento, BlogPost

admin.site.register(Proyecto)
admin.site.register(Testimonio)
admin.site.register(Crecimiento)
admin.site.register(BlogPost)