from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render

tasks = []

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)


# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []    #if there isnt a list of task in that session, return empty list
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]   #pass the list of tasks in the sess
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["tasks"]
            tasks.append(task)
            return HttpResponseRedirect("/tasks")
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    return render(request, "tasks/add.html", {
        "form": NewTaskForm
    })