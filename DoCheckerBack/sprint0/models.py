from django.db import models


# Create your models here.

class Type(models.Model):
    title = models.CharField(max_length=30)


class Client(models.Model):
    fullname = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

# class Doc(models.Model):
#     client = models.ForeignKey(Client,on_delete=models.CASCADE())
#     documentType = models.ForeignKey(DocumentType,on_delete=models.CASCADE())
