from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "name", "description", "created_at", "updated_at"]
        # or fields = '__all__' to include all fields
