from django.contrib import admin
from blogapi_postgres.models import Article


class AdminArticle(admin.ModelAdmin):
    list_display=["title", "date_created", "updated", "published"]


admin.site.register(Article, AdminArticle)