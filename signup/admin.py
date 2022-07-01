from django.contrib import admin
from signup . models import Saveuser

# Register your models here.
admin.site.register(Saveuser)


class SaveuserAdmin(admin.ModelAdmin):
    list_display=['id','studentname','city','mno','cls','collegename']


