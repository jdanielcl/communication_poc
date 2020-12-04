from django.urls import path, include
from rest_framework import routers
from .views import hello
from .views import ObjViewSet

router = routers.DefaultRouter()

router.register(r'obj', ObjViewSet)

urlpatterns = [
    path("hello", hello),
    path('', include(router.urls)),
]
