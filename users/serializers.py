from rest_framework import serializers

from users.tasks import send_email_contact, send_spam_email

from .models import Contact, Mailing, Review


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'name', 'text', 'star_rating', 'user', 'created')


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'email', 'content')

    def save(self, **kwargs):
        first_name = self.validated_data.get('first_name')
        email = self.validated_data.get('email')
        content = self.validated_data.get('content')
        send_email_contact.delay(name=first_name, email=email, content=content)


class MailingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mailing
        fields = ('id', 'email', 'date')

    def save(self, **kwargs):
        email = self.validated_data.get('email')
        send_spam_email.delay(email)
