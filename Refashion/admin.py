from django.contrib import admin
from .models import UserProfile, NGO, Product, Donation, Complaint, regtable


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "address")
    search_fields = ("user__username", "user__first_name", "user__last_name", "phone")


@admin.register(NGO)
class NGOAdmin(admin.ModelAdmin):
    list_display = ("organization_name", "email", "phone", "is_approved", "date")
    list_filter = ("is_approved",)
    search_fields = ("organization_name", "email", "phone")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "category", "price", "date")
    list_filter = ("category",)
    search_fields = ("title", "user__username")


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ("user", "ngo", "status", "date")
    list_filter = ("status",)
    search_fields = ("user__username", "ngo__organization_name")


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ("title", "sender", "date")
    search_fields = ("title", "sender__username")


@admin.register(regtable)
class RegtableAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "email", "phone_number")
    search_fields = ("firstname", "lastname", "email", "phone_number")
