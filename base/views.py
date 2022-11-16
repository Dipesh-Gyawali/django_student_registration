from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.

def index(request):
    students=Student.objects.all()
    
    form = StudentForm()
    
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')    
    
    context={'students':students, 'form':form}
    return render(request,'base/list.html',context)


def updateStudent(request, pk):
    student=Student.objects.get(id=pk)
    
    form = StudentForm(instance=student)
    
        
    if request.method=='POST':
            form = StudentForm(request.POST, instance=student)
            if form.is_valid():
                form.save()
                return redirect('/')
    
    context={'form':form}
    return render(request,'base/update_task.html',context)

def deleteStudent(request, pk):
    st=Student.objects.get(id=pk)
        
    if request.method=='POST':
                st.delete()
                return redirect('/')
    
    context={'st':st}
    return render(request,'base/delete.html',context)


