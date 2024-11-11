from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from Todo.models import Todo



# start index and add views
def home(request):
    tasks=Todo.objects.filter(is_completed=False).order_by('-updated')
    if request.method == 'POST':
        c_task=request.POST['task']
        task=Todo(task=c_task)
        task.save()
    completed_tasks=Todo.objects.filter(is_completed=True).order_by('-updated')
    
    context={
        'tasks':tasks,
        'completed_tasks':completed_tasks
        }
    return render(request,'index.html',context)
# end 