from django.contrib import admin

from .models import (Contact, EmailVerification, Mailing, Review, StarRating,
                     User)


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    readonly_fields = ('name', 'star_rating')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_verified_email')
    inlines = (ReviewInline,)


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'expiration')
    fields = ('code', 'user', 'expiration', 'created')
    readonly_fields = ('created',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email')
    fields = ('first_name', 'last_name', 'email', 'content')
    ordering = ('first_name',)


@admin.register(Review)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'star_rating')
    fields = ('name', 'text', 'user', 'star_rating', 'created')
    readonly_fields = ('created',)
    ordering = ('star_rating',)


@admin.register(StarRating)
class StarRatingAdmin(admin.ModelAdmin):
    list_display = ('value',)
    fields = ('value',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('email', 'date')
    fields = ('email',)
    readonly_fields = ('date',)
    ordering = ('date',)
