from rest_framework import viewsets, permissions, filters
from .models import MiniProject
from .serializers import MiniProjectSerializer
from django_filters.rest_framework import DjangoFilterBackend


class MiniProjectViewSet(viewsets.ModelViewSet):
    serializer_class = MiniProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['status', 'priority', 'due_date', 'assigned_to']
    ordering_fields = ['due_date', 'priority', 'created_at']

    def get_queryset(self):
        user = self.request.user
        # Safely get user.role, avoid AttributeError if role missing
        role = getattr(user, 'role', None)
        
        if role == 'trainer':
            # Trainer sees all projects
            return MiniProject.objects.all()
        else:
            # Trainee and others see only assigned projects
            return MiniProject.objects.filter(assigned_to=user)

    def perform_create(self, serializer):
        # You might want to automatically assign current user or trainer explicitly here
        # For example, ensure assigned_to is provided or default to current user
        # serializer.save(assigned_to=self.request.user)

        serializer.save()
