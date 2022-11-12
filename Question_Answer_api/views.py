from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import QuestionSerializers
from .models import Question_1


class Question1ViewSet(viewsets.ModelViewSet):
   queryset = Question_1.objects.all()
   serializer_class = QuestionSerializers


