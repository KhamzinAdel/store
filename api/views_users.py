from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from users.serializers import ReviewSerializer
from users.models import Review
from users.permissions import IsOwnerOrReadOnly


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('star_rating',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
