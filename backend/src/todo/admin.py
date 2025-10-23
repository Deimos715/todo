from django.contrib import admin

from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    '''
    Регистрация модели Todo в админке: показываем ключевые поля, включаем
    фильтры по владельцу и статусу, поиск по названию и описанию, сортировку
    по статусу и названию и фиксируем временные метки только для чтения.
    '''

    list_display = ('title', 'user', 'completed', 'created', 'updated')
    search_fields = ('title', 'memo')
    list_filter = ('completed', 'user')
    ordering = ('completed', 'title')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'updated')
