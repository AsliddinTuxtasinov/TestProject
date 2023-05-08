from rest_framework import serializers
from .models import Role


class HistoricalRoleSerializer(serializers.ModelSerializer):
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
