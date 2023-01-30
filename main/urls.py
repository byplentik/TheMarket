from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('<slug:slug>/', CategoryDetailView.as_view(), name='category_detail')
]
