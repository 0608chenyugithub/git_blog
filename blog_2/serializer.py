from django.contrib.auth.models import User, Group
from rest_framework import serializers
from blog_2.models import *


class PythonTitleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PythonTitle
        fields = ('title',)


class PythonSubTitleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PythonSubTitle
        fields = ('sub_title', 'detail')