from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from rest_api.views import hello
from rest_api.views import ObjViewSet

router = routers.DefaultRouter()

router.register(r'obj', ObjViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('rest/', include('rest_api.urls')),
    path('', include(router.urls)),
]
