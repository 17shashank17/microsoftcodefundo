from django.shortcuts import render
from todolist.forms import input
from todolist.models import liste

def main_page(request):
    to_do=liste.objects.values_list('list_todo',flat=True).order_by('-id')    #returns a list containing tasks which is sorted in descending order by id
    form = input()
    if request.method=="POST":
        form=input(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"todolist/todolist.html",{"to_do":to_do,"form":form,})
        else:
            form=input()
            return render(request,"todolist/todolist.html",{"to_do":to_do,"form":form,})


    return render(request,"todolist/todolist.html",{"to_do":to_do,"form":form,})


