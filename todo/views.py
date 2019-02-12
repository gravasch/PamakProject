from django.shortcuts import render
from .models import TodoItem
from django.http import HttpResponseRedirect


def todoview(request):
    all_todo_items = TodoItem.objects.all()
    return render(request=request, template_name="todo/todo.html",
                  context={'all_items': all_todo_items})


def addtodo(request):
    new_item = TodoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')

    # create a todo all_items
    # save
    # redirect browser to '/todo/'


def deltodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')
