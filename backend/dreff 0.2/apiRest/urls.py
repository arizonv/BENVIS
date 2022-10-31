from django.contrib import admin
from django.urls import path
from apiRest.views import developerCreate, developerDelete, developerUpdata

urlpatterns = [
    path('api/developer/', developerCreate.as_view()),

    path('api/developer/<pk>/', developerDelete.as_view()),

    path('api/developerUp/<pk>/', developerUpdata.as_view()),
]
