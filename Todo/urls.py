from django.urls import path
from .import views

urlpatterns = [
   
   # mark_as_done
    path('mark_as_done/<int:pk>/',views.mark_as_done,name="mark_as_done"),
    
    # mark_as_undone
    path('mark_as_undone/<int:pk>/',views.mark_as_undone,name="mark_as_undone"),
    
    # edit
    path('edit/<int:pk>/',views.edit,name="edit_page"),
    
    # delete
    path('delete/<int:pk>/',views.delete,name="deletepage"),
    
    
]