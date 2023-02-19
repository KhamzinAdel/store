from django.contrib import admin

from products.admin import BasketAdmin

from .models import Contact, EmailVerification, User, Reviews, StarRating


class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'star_rating')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_verified_email')
    inlines = (BasketAdmin, ReviewInline)


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


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'star_rating')
    fields = ('name', 'text', 'user', 'star_rating', 'created')
    readonly_fields = ('created',)
    ordering = ('star_rating',)


@admin.register(StarRating)
class StarRatingAdmin(admin.ModelAdmin):
    list_display = ('value',)
    fields = ('value',)
