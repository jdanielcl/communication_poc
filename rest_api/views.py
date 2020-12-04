from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import ObjSerializer
from .models import Obj


def hello(request):
    return HttpResponse("hello", 200)


class ObjViewSet(viewsets.ModelViewSet):
    serializer_class = ObjSerializer
    queryset = Obj.objects.all()
