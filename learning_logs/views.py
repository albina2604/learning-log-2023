from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Topic
from .forms import TopicForm, EntryForm

# Create your views here.


def index(request):
    """Головна сторінка додатку Learning Log"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Виводить список тем"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Виводить одну тему і всі ії записи"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """Додає нову тему"""
    if request.method != 'POST':
        # Дані не відправлялись, створюється пуста форма
        form = TopicForm()
    else:
        # Обробка даних з форми
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """Додає новий запис до певної теми"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry_object = form.save(commit=False)
            new_entry_object.topic = topic
            new_entry_object.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    context = {'form': form, 'topic': topic, }
    return render(request, 'learning_logs/new_entry.html', context)
