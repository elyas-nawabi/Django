from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer,SnippetSerializer
from .models import Moviedata,Snippet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializer
class ActionViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='action')
    serializer_class  = MovieSerializer
class ComedyViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='comedy')
    serializer_class  = MovieSerializer
class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

    # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])/
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
# class UserViewSet(viewsets.ModelViewSet):
#     """
#     This viewset automatically provides `list` and `retrieve` actions.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
