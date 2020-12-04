from rest_framework import serializers
from .models import Obj


class ObjSerializer(serializers.ModelSerializer):

    class Meta:
        model = Obj
        fields = [
            "text"
        ]
