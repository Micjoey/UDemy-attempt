
from django.shortcuts import render

from quizzes.models import Quiz


def index(request):
    context = {
        'questions': Quiz.objects.all(),
    }
    return render(request, 'quiz/question_list.html', context)


def show(request, id):
    context = {
        'question': Quiz.objects.get(id=id),
    }
    return render(request, 'quiz/question.html', context)
