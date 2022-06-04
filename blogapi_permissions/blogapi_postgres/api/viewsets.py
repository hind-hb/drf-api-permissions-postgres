from rest_framework.generics import (
                                        ListCreateAPIView,
                                        RetrieveUpdateAPIView
                                    )

from blogapi_postgres.models import Article
from .serializers import ArticleSerializer
from .permissions import IsOwnerOrReadOnly 
from rest_framework.permissions import IsAuthenticated

class ArticlesListView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    


class ArticlesDetailView(RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsOwnerOrReadOnly,IsAuthenticated  )