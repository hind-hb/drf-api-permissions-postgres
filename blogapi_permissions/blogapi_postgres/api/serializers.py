from rest_framework import serializers
from blogapi_postgres.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('title','date_created','updated' ,'author', 'content', 'published')