from django.shortcuts import render , redirect
from .models import COURSE
from .forms import CourseForm
# Create your views here.

### Function Based Views
def course_list(request):
    all = COURSE.objects.all()
    return render(request,'courses.html',{'data':all})

def course_detail(request,id):
    course = COURSE.objects.get(id=id)
    return render(request,'single.html',{'data':course})

def add_course(request):
    if request.method == 'POST':
        print('in post ...')
        form = CourseForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
    else:
        print(' in get ...')
        form = CourseForm()
    return render(request,'add.html',{'form':form})



def edit_course(request,id):
    course = COURSE.objects.get(id=id)
    if request.method == 'POST':
        print('in post ...')
        form = CourseForm(request.POST,request.FILES,instance=course)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
    else:
        print(' in get ...')
        form = CourseForm(instance=course)
    return render(request,'edit.html',{'form':form})


def delete_course(request,id):
    course = COURSE.objects.get(id=id)
    course.delete()
    return redirect('/udemy')


#### Class Based Views 
from django.views.generic import ListView


class CourseList(ListView):
    model = COURSE
    template_name = 'courses.html'