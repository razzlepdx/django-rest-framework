from django.shortcuts import render
from rest_framework import viewsets
from .models import Paradigm, Language, Programmer
from .serializers import ParadigmSerializer, LanguageSerializer, ProgrammerSerializer

class ParadigmView(viewsets.ModelViewSet):

    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer

class LanguageView(viewsets.ModelViewSet):

    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class ProgrammerView(viewsets.ModelViewSet):

    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
