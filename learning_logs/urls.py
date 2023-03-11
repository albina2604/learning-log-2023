"""Визначає схеми URL для learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Домашня сторінка
    path('', views.index, name='index'),
    # Сторінка з переліком усіх тем
    path('topics/', views.topics, name='topics'),
    # Сторінка з докладною інформацією за окремою темою
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Сторінка для додавання нової теми
    path('new_topic/', views.new_topic, name='new_topic'),
    # Сторінка для додавання нового запису
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

]
