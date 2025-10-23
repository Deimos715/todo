from rest_framework import generics
from src.todo.models import Todo
from .serializers import TodoSerializer, TodoToggleCompleteSerializer
from rest_framework import generics, permissions


class TodoListCreate(generics.ListCreateAPIView):
    '''
    Классовое представление списка и создания задач: применяет TodoSerializer
    и работает только с записями текущего пользователя.
    '''

    serializer_class = TodoSerializer
    # доступ только для авторизованных
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        '''Возвращаем задачи авторизованного пользователя, отсортированные по дате.'''
        user = self.request.user
        return Todo.objects.filter(user=user).order_by('-created')

    def perform_create(self, serializer):
        '''При сохранении новой задачи подставляем текущего пользователя.'''
        serializer.save(user=self.request.user)


class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    '''
    Классовое представление для работы с одной задачей: позволяет
    авторизованному пользователю получить, изменить или удалить только
    собственный объект Todo.
    '''

    serializer_class = TodoSerializer
    # доступ только для авторизованны
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        # пользователь может только обновлять, удалять собственные записи
        return Todo.objects.filter(user=user)


class TodoToggleComplete(generics.UpdateAPIView):
    '''
    Классовое представление для завершения задачи: позволяет
    авторизованному пользователю отметить задачу как выполненную.
    '''

    serializer_class = TodoToggleCompleteSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        # пользователь может только обновлять, удалять собственные записи
        return Todo.objects.filter(user=user)
    
    def perform_update(self,serializer):
        serializer.instance.completed=not(serializer.instance.completed)
        serializer.save()