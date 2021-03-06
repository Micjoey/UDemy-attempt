from rest_framework import serializers

from quizzes.models import Quiz

class MathQuizSerializer(serializers.ModelSerializer):
    question = serializers.CharField(min_length=2, max_length=200)
    answer = serializers.DecimalField(
        min_value=1.00, max_value=100000,
        max_digits=None, decimal_places=2,
    )
    
    class Meta:
        model = Quiz
        fields = (
            'id', 'title', 'answer', 
        )
