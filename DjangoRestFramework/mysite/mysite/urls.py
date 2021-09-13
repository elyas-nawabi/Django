from django.contrib import admin
from django.urls import include,path
from rest_framework import routers
from movies.views import MovieViewSet,ActionViewSet,ComedyViewSet,SnippetViewSet
from django.conf.urls.static import static
from django.conf import settings

from rest_framework.routers import DefaultRouter
# from drf.mysite.movies import views

router = routers.SimpleRouter()
router.register('movies', MovieViewSet)
router.register('action',ActionViewSet)
router.register('comedy',ComedyViewSet)
router.register('snippets', SnippetViewSet)
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
