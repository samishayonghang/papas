from django.db import models

# Create your models here.
class Personal(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='media')

class Blogs(models.Model):

    title=models.CharField(max_length=250)
    description=models.TextField()
    photos=models.ImageField(upload_to='blogs/', height_field=None, width_field=None, )
    uploaddate=models.DateTimeField(auto_now=True)



class Contact(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    mobile=models.IntegerField()
    message=models.CharField( max_length=500)


