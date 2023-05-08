from rest_framework import viewsets

from testProject.models import Role
from testProject.serializers import RoleSerializer


class RoleViews(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
