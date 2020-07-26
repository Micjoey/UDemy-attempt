
from django.shortcuts import render

from quizzes.models import Question


def index(request):
    context = {
        'question': Question.objects.all(),
    }
    return render(request, 'quizzes/question_list.html', context)


def show(request, id):
    context = {
        'question': Question.objects.get(id=id),
    }
    return render(request, 'quizzes/question.html', context)
