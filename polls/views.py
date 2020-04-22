

from django.http import HttpResponse
from django.utils import timezone
from rest_framework.viewsets import  ModelViewSet

from .models import Question
from .serializers import QuestionSerializer

from rest_framework.decorators import action


class PollsViewSet(ModelViewSet):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    @action(methods=['get'], url_path='temp',detail=False)
    def index(self, request, *args, **kwargs):
        return HttpResponse("Hello, world. You're at the polls index.")

    @action(methods=['post'], url_path='insert', detail=False)
    def insert_question(self, request, *args, **kwargs):
        question_text = request.GET.get('q', 'Default question')
        question_type = request.GET.get('type', 'M')
        q = Question(question_text=question_text, pub_date=timezone.now(), question_type=question_type)
        q.save()
        return HttpResponse(q)
