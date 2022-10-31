from dataclasses import fields
from django import forms
from .models import Developer
from rest_framework import serializers


class developerSerializer (serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'