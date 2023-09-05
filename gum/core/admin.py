from django.contrib import admin
from core.models import *
# Register your models here.


admin.site.register(Ad)

@admin.register(Item)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "price",
        "date",
        "available",
        "owner",
        "description",
    )

    search_fields = ("title", "category", "owner", "published_time")
    list_filter =("category", "available", )

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "type",
        "salary",
        "date",
        "available",
        "owner",
        "description",
        "heures",
        "website",
        "contract_type",
        "period",
    )

    search_fields = ("title", "category", "owner", "published_time")
    list_filter =("category", "available", )

admin.site.register(Category)

admin.site.register(Category_job)

admin.site.register(Subcategory)

admin.site.register(Type)

admin.site.register(Characteristics)

admin.site.register(Item_Characteristics)

admin.site.register(Job_Characteristics)

admin.site.register(PhoneNumber)

admin.site.register(ImageModel)

admin.site.register(Languages)

admin.site.register(Niveau)