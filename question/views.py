from rest_framework import viewsets
from .serializers import QuestionSerializer, OptionSerializer, StudentQuestionSerializer
from .models import Question, Options, StudentQuestion

# Create your views here.
class QuestionViewSet(viewsets.ModelViewSet):
    '''A simple crud for courses'''
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    
class OptionViewSet(viewsets.ModelViewSet):
    '''A simple crud for courses'''
    serializer_class = OptionSerializer
    queryset = Options.objects.all()
    
class StudentQuestionViewSet(viewsets.ModelViewSet):
    '''A simple crud for courses'''
    serializer_class = StudentQuestion
    queryset = StudentQuestion.objects.all()