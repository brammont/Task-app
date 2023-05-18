from rest_framework import serializers
from .models import Task
class TaskSerializers(serializers.ModelSerializer):
    class Mets:
        model = Task
        #fields = ('id','title','description','done')
        fields = '__all__'