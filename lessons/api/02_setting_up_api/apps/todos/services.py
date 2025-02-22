from .models import Todo


def get_todo_list():
    return Todo.objects.all().order_by("-created_at")


def get_todo_by_id(pk):
    try:
        return Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return None


def create_todo(name, description=None, status="pending"):
    return Todo.objects.create(
        name=name,
        description=description,
        status=status,
    )


def update_todo_by_id(pk, data):
    todo = get_todo_by_id(pk)
    if todo:
        for key, value in data.items():
            setattr(todo, key, value)
        todo.save()
    return todo


def delete_todo_by_id(pk):
    todo = get_todo_by_id(pk)
    if todo:
        todo.delete()
    return todo
