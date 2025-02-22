from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Todo
from .serializers import TodoSerializer
from .services import (
    get_todo_list,
    get_todo_by_id,
    create_todo,
    update_todo_by_id,
    delete_todo_by_id,
)


@api_view(["GET", "POST"])
def todo_list_create(request):
    if request.method == "GET":
        todos = get_todo_list()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            todo = create_todo(**serializer.validated_data)
            serializer = TodoSerializer(todo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def todo_detail_update_delete(request, pk):
    todo = get_todo_by_id(pk)
    if not todo:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    elif request.method in ["PUT", "PATCH"]:
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            updated_todo = update_todo_by_id(pk, serializer.validated_data)
            serializer = TodoSerializer(updated_todo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        delete_todo_by_id(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
