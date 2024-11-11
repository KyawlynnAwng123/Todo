from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from .models import Todo




# start mark_as_done views
def mark_as_done(request,pk):
    task=get_object_or_404(Todo,pk=pk)
    task.is_completed=True
    task.save()
    return redirect('homepage')
# end

# start mark_as_undone views
def mark_as_undone(request,pk):
    task=get_object_or_404(Todo,pk=pk)
    task.is_completed=False
    task.save()
    return redirect('homepage')
# end

# start edit views
def edit(request,pk):
    task=get_object_or_404(Todo,pk=pk)
    if request.method == 'POST':
        e_task=request.POST['task']
        task.task=e_task
        task.save()
        return redirect('homepage')
        
    else:
        
        context={
            'task':task
            }
        return render(request,'crud/edit.html',context)
# end

# start delete views
def delete(request,pk):
    task=get_object_or_404(Todo,pk=pk)
    task.delete()
    return redirect('homepage')
# end delete views










        