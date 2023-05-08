from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Role


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'first_name', 'last_name']


class HistoricalRoleSerializer(serializers.ModelSerializer):
    history_user = UserSerializer()

    class Meta:
        model = Role.history.model
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    history = serializers.SerializerMethodField()

    class Meta:
        model = Role
        fields = "__all__"

    @staticmethod
    def get_history(obj):
        history = obj.history.all()
        serialized_history = []
        for index, h in enumerate(history):
            old_data = HistoricalRoleSerializer(history[index - 1]).data if index > 0 else None
            new_data = HistoricalRoleSerializer(h).data
            new_data['old_history'] = old_data
            serialized_history.append(new_data)
        return serialized_history
