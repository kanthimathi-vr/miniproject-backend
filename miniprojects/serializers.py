from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import MiniProject

User = get_user_model()

class MiniProjectSerializer(serializers.ModelSerializer):
    assigned_to = serializers.SlugRelatedField(
        slug_field="email",
        queryset=User.objects.all()  # Provide queryset here
    )
    
    class Meta:
        model = MiniProject
        fields = '__all__'
