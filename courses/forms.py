from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        fields = ['title','subtitle','requirements','description','course_content','language','price']
        #exclude = ('author',)