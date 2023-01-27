from django.shortcuts import render , redirect
from .models import Course
from .forms import CourseForm
# Create your views here.

def course_list(request):
    all = Course.objects.all()
    return render(request, 'courses.html',{'data':all})

def course_detail(request,id):
    course = Course.objects.get(id=id)
    return render(request, 'single.html' , {'data':course})

def add_course(request):
    if request.method == 'COURSE':
        print('in post ...')
        form = CourseForm(request.COURSE,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
    else:
        print(' in get ...')
        form = CourseForm()
    return render(request,'add.html',{'form':form})