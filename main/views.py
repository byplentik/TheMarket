from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Product, Category
from .forms import ReviewForm


class HomeListView(generic.ListView):
    template_name = 'main/homelist.html'
    model = Product


class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'main/categories.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category=self.object)
        return context


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'main/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewForm
        return context


class AddReviewView(generic.CreateView):
    form_class = ReviewForm
    template_name = 'main/product_detail.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        product = get_object_or_404(Product, slug=self.kwargs['slug'])
        form.instance.product = product
        return super().form_valid(form)
    

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')


    


    
    
