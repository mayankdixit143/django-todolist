from django.shortcuts import render, redirect
from .models import ToDo
from .serializers import TodoSerializer
from rest_framework import viewsets
from django.http import JsonResponse

# Create your views here.
def show_all(request):
    objs = ToDo.objects.all().order_by('deadline')
    return render(request, 'todo/index.html', context={'list':objs})

def add(request):
    if request.method == "POST":
        obj = ToDo(task = request.POST["task"])
        obj.save()
        return redirect(show_all)

def update_task(request):
    if request.method == "POST":
        obj = ToDo.objects.get(id = request.POST['id'])
        obj.task = request.POST['taskname']

        if request.POST.get('completed', False) == 'on':
            obj.is_completed = True
        else:
            obj.is_completed = False
        obj.save()

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
