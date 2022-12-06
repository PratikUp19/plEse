from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

class article(models.Model):
    a_id=models.UUIDField(primary_key=True,default = uuid.uuid4)
    a_title=models.CharField(max_length=30)
    a_description=models.CharField(max_length=1000)
class BlogComment(models.Model):
    c_id=models.UUIDField(primary_key=True,default = uuid.uuid4)
    comment=models.CharField(max_length=30)
    user=models.CharField(max_length=300)
    artic=models.CharField(max_length=300)
