from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<slug:slug>/add-review/', AddReviewView.as_view(), name='add_review'),
    path('product/<slug:slug>/update-review/<int:review_id>/', UpdateReviewView.as_view(), name='update_review'),
    path('product/<slug:slug>/delete-review/<int:review_id>/', DeleteReviewView.as_view(), name='delete_review'),
]