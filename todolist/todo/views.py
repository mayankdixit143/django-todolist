from django.shortcuts import render, redirect
from .models import ToDo
from .serializers import TodoSerializer
from rest_framework import viewsets
from django.http import JsonResponse

# Create your views here.
def show(flag=0):
    if flag==1:
        objs = list(ToDo.objects.all().filter(is_completed=False).order_by('deadline'))
        objs = objs + list(ToDo.objects.all().filter(is_completed=True).order_by('deadline'))
    elif flag==2:
        objs = list(ToDo.objects.all().filter(is_completed=False).order_by('created_at'))
        objs = objs + list(ToDo.objects.all().filter(is_completed=True).order_by('created_at'))
    else:
        objs = list(ToDo.objects.all().filter(is_completed=False))
        objs = objs + list(ToDo.objects.all().filter(is_completed=True))
    return objs

def show_by_deadline(request):
    return render(request, 'todo/index.html', context={'list':show(flag=1)})

def show_by_created_at(request):
    return render(request, 'todo/index.html', context={'list':show(flag=2)})

def show_all(request):
    return render(request, 'todo/index.html', context={'list':show()})


def add(request):
    if request.method == "POST":
        print(request.POST)
        obj = ToDo(task = request.POST["taskname"],
                    description = request.POST["description"])
        obj.save()
        return redirect(show_all)

def update_task(request):
    if request.method == "POST":
        obj = ToDo.objects.get(id = request.POST['id'])

        obj.task = request.POST['taskname']
        obj.description = request.POST.get('description', "desc_def")

        if request.POST.get('completed', False) == 'on':
            obj.is_completed = True
        else:
            obj.is_completed = False

        obj.save()
        return redirect(show_all)

def delete(request, id):
    if request.method == "GET":
        ToDo.objects.get(id = id).delete()
        return redirect(show_all)

def clear(request):
    if request.method == "GET":
        ToDo.objects.all().delete()
        return redirect(show_all)


# class TodoViewSet(viewsets.ModelViewSet):
#     queryset = ToDo.objects.all().order_by('deadline')
#     serializer_class = TodoSerializer
#
#     def list(self, request):
#         render(request, 'todo/index.html', context={'list':'hi'})
#
#     def create(self, request):
#         render(request, 'todo/index.html', context={'list':'hi'})
#
#     def update(self, request, pk=None):
#         pass
