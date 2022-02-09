from rest_framework.viewsets import ModelViewSet


from .models import Author
from .serializers import AuthorsModelSerializer
class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()