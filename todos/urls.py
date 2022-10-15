from django.urls import path
from todos import views 

app_name = 'todos'
urlpatterns = [
  path('', views.TodoListView.as_view(), name="todos_list"),
  path('<int:id>/', views.TodoView.as_view(), name="todos_detail"),
  path('<int:id>/check/', views.TodoCheckView.as_view(), name="todos_check"),

]