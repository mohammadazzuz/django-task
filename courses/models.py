from django.db import models
from django.contrib.auth.models import User
from languages.fields import LanguageField

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=1000)
    subtitle = models.TextField(max_length=5000)
    author = models.ForeignKey(User,related_name='course_author',on_delete=models.CASCADE)
    date_modified = models.DateTimeField(auto_now=True)
    language = LanguageField()
    course_content = models.TextField(max_length=100000000000)
















    def __str__(self):
        return self.title
    

