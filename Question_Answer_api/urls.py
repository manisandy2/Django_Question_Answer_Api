from django.urls import include, path
from rest_framework import routers
from .views import Question1ViewSet


router = routers.DefaultRouter()
router.register(r'qus', Question1ViewSet)


urlpatterns = [
   path('', include(router.urls)),
]