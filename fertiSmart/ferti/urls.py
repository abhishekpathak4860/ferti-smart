from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('soil-analysis', views.soilAnalysis, name='soilAnalysis'),
    path('crop-yield', views.cropYield, name='cropYield'),
    path('sustainability', views.sustainability, name='sustainability'),
    path('fertilizer', views.fertilizer, name='fertilizer'),
    path('about', views.about, name='about'),
]
