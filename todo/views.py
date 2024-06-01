from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from todo.models import Task
from todo.serializers import TaskSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def index(request, pk=None):

    if request.method == 'GET':
        task_list = Task.objects.all()
        serializer = TaskSerializer(task_list, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'PUT':
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(task, dat=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        task = Task.objects.get(id=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['POST'])
# def create_task(request):
#     serializer = TaskSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['PUT'])
# def update_task(request, pk):
#     task = Task.objects.get(id=pk)
#     serializer = TaskSerializer(task, dat=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['DELETE'])
# def delete_task(request, pk):
#     task = Task.objects.get(id=pk)
#     task.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)
