from django.urls import path

from .views import todo_list_create, todo_detail_update_delete

urlpatterns = [
    path("todos/", todo_list_create, name="todo_list_create"),
    path(
        "todos/<int:pk>/", todo_detail_update_delete, name="todo_detail_update_delete"
    ),
]
