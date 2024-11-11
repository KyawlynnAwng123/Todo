from django.db import models


# start todo model
class Todo(models.Model):
    task=models.CharField(max_length=100)
    is_completed=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.task
    

# end

