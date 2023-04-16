from django.urls import path

from .views import ProfileTemplateView

urlpatterns = [
    path('<slug:slug>/', ProfileTemplateView.as_view(), name='user_detail'),
]
