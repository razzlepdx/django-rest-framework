from rest_framework import serializers
from .models import Paradigm, Language, Programmer

class ParadigmSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Paradigm
        fields = ('id', 'url', 'name')

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    """ Defines the LanguageSerializer class. """

    class Meta:
        model = Language
        fields = ('id', 'url', 'name', 'paradigm')

class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Programmer
        fields = ('id', 'url', 'name', 'languages')