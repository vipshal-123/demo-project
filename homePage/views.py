from django.shortcuts import render,redirect
from homePage.models import Tasklist
from homePage.forms import Task
from django.contrib import messages
from django.core.paginator import Paginator


def homes(request):
    if(request.method == 'POST'):
        form = Task(request.POST or None)
        if(form.is_valid()):
            form.save()
        messages.success(request,"You have successfully added the Task")
        return redirect('homes') 
    else:    
        all_text = Tasklist.objects.all()
        paginator = Paginator(all_text,5)
        page = request.GET.get('pg')
        all_text = paginator.get_page(page)
        
        return render(request, 'index_home.html',{'all_text':all_text})
    
def delete(request,task_id):
    task = Tasklist.objects.get(pk = task_id)
    task.delete()
    return redirect('homes')

def edit(request, task_id):
    if(request.method == 'POST'):
        edit = Tasklist.objects.get(pk = task_id)
        form = Task(request.POST or None, instance= edit)
        if(form.is_valid()):
            form.save()
        messages.success(request,"You have successfully Updated")
        return redirect('homes') 
    else:    
        edit_text = Tasklist.objects.get(pk = task_id)
        return render(request, 'edit.html',{'edit_text':edit_text})
    
def complete(request,task_id):
    task = Tasklist.objects.get(pk = task_id)
    task.done = True
    task.save()
    return redirect('homes')

def notcomplete(request,task_id):
    task = Tasklist.objects.get(pk = task_id)
    task.done = False
    task.save()
    return redirect('homes')

def contact(request):
    context = {
        'text' : 'Hi Hello, this is Contact Us page',
      
    }
    return render(request,'contactus.html',context)

def about(request):
    context = {
        'text' : 'Hi Hello, this is about Us page',
        
    }
    return render(request,'aboutus.html',context)