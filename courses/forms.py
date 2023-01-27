from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        #   fields = ['title','content','image','tags','comment']
        #exclude = ('author',)