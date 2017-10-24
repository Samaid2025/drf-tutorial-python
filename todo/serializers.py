from rest_framework import serializers

from todo.models import ToDo
from todo.models import Uploads

class ToDoSerializer(serializers.Serializer):
    class Meta:
        model = ToDo
        fields = 'id', 'text', 'done'


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = 'id', 'text', 'done'


class UploadsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Uploads
        fields = 'name', 'ip','file'


