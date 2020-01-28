"""tsp_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    path('arama/', views.arama, name='arama'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('lisans/', views.lisans, name='lisans'),
    path('hesap/', views.hesap, name='hesap'),
    path('mamul/', views.mamul, name='mamul'),
    path('hammadde/', views.hammadde, name='hammadde'),
    path('mamulrapor/', views.mamulrapor, name='mamulrapor'),
    path('hammadderapor/', views.hammadderapor, name='hammadderapor'),
]
