from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, \
    RetrieveUpdateDestroyAPIView, GenericAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from quizzes.serializers import MathQuizSerializer
from quizzes.models import Quiz


class QuizPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

class QuizzesList(ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = MathQuizSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    search_fields = ('question',)
    pagination_class = QuizPagination
    queryset
