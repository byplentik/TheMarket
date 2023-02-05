from django.views import generic

from .models import Product, Category, Review


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