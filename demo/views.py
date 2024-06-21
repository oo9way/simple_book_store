from django.shortcuts import render
from django.views.generic import TemplateView
from django.http.response import HttpResponse
from demo.models import Todo


def todo_app(request):
    messages = {
        "todolar": Todo.objects.all().order_by("-id")
    }

    if request.method == "POST":
        vazifa = request.POST['task']
        Todo.objects.create(task=vazifa)

    # if request.method == "GET":
    #     messages['xabar'] = request.GET['xabar']
    
    
    return render(request, "index.html", context=messages)