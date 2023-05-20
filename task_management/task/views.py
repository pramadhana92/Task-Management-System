from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Task
from .serializers import TaskSerializer

class TaskListAPI(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            # set id manually if id provided
            if 'id' in request.data:
                new_id = request.data['id']
                serializer.save(id=new_id)
            else:
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetailAPI(APIView):
    def get_object(self, task_id):
        try:
            return Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return None

    def get(self, request, task_id): 
        task = self.get_object(task_id)
        if not task:
            return Response(
                {"response": "Object with task id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, task_id):
        task = self.get_object(task_id)
        if not task:
            return Response(
                {"response": "Object with task id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = TaskSerializer(instance=task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, task_id):
        task = self.get_object(task_id)
        if not task:
            return Response(
                {"response": "Object with task id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        task.delete()
        return Response(
            {"response": "Object deleted"},
            status=status.HTTP_200_OK
        )