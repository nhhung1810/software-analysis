from django.urls import path
from .views import views, detectorView

urlpatterns = [
    path('', views.index, name='index'),
    path('detect', detectorView.detect, name='detect'),
]