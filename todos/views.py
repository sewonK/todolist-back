import json
from django.views.generic import View
from .models import Todo
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

def todo_instance_to_dictionary(todo):
  result = {}
  result["id"] = todo.id
  result["text"] = todo.text
  result["done"] = todo.done
  return result

@method_decorator(csrf_exempt, name = "dispatch")
class TodoListView(View):
  def get(self, request):
    try:
      todo_list = []
      todo_queryset = Todo.objects.all()
      for todo_instance in todo_queryset:
        todo_list.append(todo_instance_to_dictionary(todo_instance))

      data = { "todos": todo_list }
      return JsonResponse(data, status=200)
    except:
      return JsonResponse({"msg": "Failed to get todos"}, status=404)

  def post(self, request):
    try:
      body = json.loads(request.body) #body에서 받아온 것을 역직렬화!
    except:
      return JsonResponse({"msg": "Invalid parameters"}, status=400)

    try:
      todo_instance = Todo.objects.create(text=body["text"])
    except:
      return JsonResponse({"msg": "Failed to create todos"}, status=400)

    todo_dict = todo_instance_to_dictionary(todo_instance)
    data = { "todo": todo_dict }
    return JsonResponse(data, status=200)

@method_decorator(csrf_exempt, name = "dispatch")
class TodoCheckView(View):
  def patch(self, request, id):
    try:
      todo_instance = Todo.objects.get(id=id)
      todo_instance.check_todo()
      todo_dict = todo_instance_to_dictionary(todo_instance)
      data = { "todo": todo_dict }
      return JsonResponse(data, status=200)
    except:
      return JsonResponse({"msg": "Failed to create todos"}, status=404)

@method_decorator(csrf_exempt, name = "dispatch")
class TodoView(View):
  def get(self, request, id):
    try:
      todo_instance = Todo.objects.get(id=id)
      todo_dict = todo_instance_to_dictionary(todo_instance)
      data = { "todo": todo_dict }
      return JsonResponse(data, status=200)
    except:
      return JsonResponse({"msg": "Failed to edit todo"}, status=404)
  
  def delete(self, request, id):
    try:
      todo_instance = Todo.objects.get(id=id)
      todo_instance.delete()
      todo_dict = todo_instance_to_dictionary(todo_instance)
      data = { "todo": todo_dict }
      return JsonResponse(data, status=200)
    except:
      return JsonResponse({"msg": "Failed to delete todo"}, status=404)