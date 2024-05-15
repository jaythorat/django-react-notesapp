# serializer helps to convert json to python and vice versa and lang can be anything
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']
        extra_kwargs = {'password':{"write_only": True}} # Telling jango that password is write only so dont return pass while reading user

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
     
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'author']
        extra_kwargs = {'author': {'read_only': True}}   # tells system that we are going to assign automatically its readonly attribute in this case
        