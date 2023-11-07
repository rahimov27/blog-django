from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm
from django.http import Http404
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    return render(request, "index.html")


@login_required
def topics(request):
    """Выводит список тем."""
    topics = Topic.objects.filter(owner=request.user).order_by("date_added")
    context = {"topics": topics}
    return render(request, "topics.html", context)


@login_required
def topic(request, topic_id):
    """Выводит список тем."""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries}
    return render(request, "topics.html", context)


@login_required
def new_topic(request):
    """Определяет новую тему."""
    if request.method != "POST":
        # Данные не отправлялись; создается пустая форма.
        form = TopicForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("learning_logs:topics")

    # Вывести пустую или недействительную форму.
    context = {"form": form}
    return render(request, "new_topic.html", context)
