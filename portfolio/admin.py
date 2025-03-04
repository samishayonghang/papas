from django.contrib import admin
from.models import Contact,Blogs

# Register your models here.
@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display=['name','email','mobile','message']

@admin.register(Blogs)
class BlogsModelAdmin(admin.ModelAdmin):
    list_display=['title','description','photos','uploaddate']