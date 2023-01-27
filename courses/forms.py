from django import forms
from .models import COURSE


class CourseForm(forms.ModelForm):
    class Meta:
        model = COURSE
        fields = '__all__'
        fields = ['title','subtitle','requirements','description','course_content','language','price']
        #exclude = ('author',)