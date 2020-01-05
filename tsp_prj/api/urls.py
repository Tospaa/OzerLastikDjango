from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('ayakkabi/', views.AyakkabiList.as_view()),
    path('ayakkabi/<int:pk>/', views.AyakkabiDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)