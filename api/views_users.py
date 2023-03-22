from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from users.serializers import ReviewSerializer, ContactSerializer, MailingSerializer
from users.models import Review
from users.permissions import IsOwnerOrStaffOrReadOnly


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsOwnerOrStaffOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('star_rating',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ContactCreateAPIView(CreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)


class MailingCreateAPIView(CreateAPIView):
    serializer_class = MailingSerializer
    permission_classes = (IsAuthenticated,)
