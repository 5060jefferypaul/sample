from django.db import models


class itemDetails(models.Model):
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=100,null=True)
    qualifications = models.CharField(max_length=100,null=True)
    image = models.ImageField(blank=True,upload_to="image/",default='static/images/Image 13.jpg', null=True)


# Create your models here.
