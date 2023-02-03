from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.urls import reverse

from .forms import RatingForm
from .models import Product, Category


class HomeListView(generic.ListView):
    template_name = 'main/homelist.html'
    model = Product

    def get_queryset(self):
        return Product.objects.all().order_by('-rating')


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
        if self.request.method == 'POST':
            context['form'] = RatingForm(self.request.POST)
        else:
            context['form'] = RatingForm()
        return context


class ProductRatingView(generic.FormView):
    form_class = RatingForm
    template_name = 'main/product_detail.html'

    def form_valid(self, form):
        product = get_object_or_404(Product, slug=self.kwargs.get('slug'))
        product.rating = form.cleaned_data['rating']
        product.save()
        return redirect(product.get_absolute_url())

    def get_success_url(self):
        return reverse('product_detail', kwargs={'slug': self.kwargs.get('slug')})


