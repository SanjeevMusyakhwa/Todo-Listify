from django.shortcuts import render, redirect
from app.models import Todo
from django.http import HttpResponseRedirect
 
# Create your views here.
def todoList(request):
  todos = Todo.objects.all()
  return render(
    request,
    'todoList.html',
    {'todos': todos}
  )
def todoCreate(request):
  if request.method == 'POST':
    title = request.POST['title']
    description = request.POST['description']
    todo = Todo.objects.create(title= title, description= description)
    todo.save()
    return redirect('todoList')
  else:
    return render(
      request,
      'todoCreate.html',
  )

def todoDelete(request, pk):
  todo = Todo.objects.get(id = pk)
  todo.delete()
  return redirect('todoList')

def todoUpdate(request, pk):
  todo = Todo.objects.get(id = pk)
  if request.method == 'POST':
    title = request.POST['title']
    description = request.POST['description']
    todo.title = title
    todo.description = description
    todo.save()
    return redirect('todoList')
  else:
    todo = Todo.objects.get(id = pk)
    return render(
      request,
      'todoUpdate.html',
      {'todo': todo}
    )