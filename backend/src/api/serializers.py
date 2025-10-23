from rest_framework import serializers
from src.todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    '''
    Сериализатор модели Todo: формирует поля для API и оставляет временные
    метки и статус выполнения доступными только для чтения.
    '''

    created = serializers.ReadOnlyField()
    updated = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()

    class Meta:
        model = Todo
        fields = ['id', 'title', 'memo', 'created', 'updated', 'completed']


class TodoToggleCompleteSerializer(serializers.ModelSerializer):
    '''
    Узкий сериализатор для переключения статуса: пропускаем только id,
    остальные поля задачи оставляем доступными лишь для чтения.
    '''
    class Meta:
        model = Todo
        fields = ['id']
        read_only_fields = ['title','memo','created', 'updated', 'completed']
