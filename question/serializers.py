from rest_framework import serializers
from .models import Question, Options, StudentQuestion

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question','qr_url', 'class_id']
        
class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ['description','question_id']
        
class StudentQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentQuestion
        fields = ['student_code', 'question_id', 'answer']
