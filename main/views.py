from django.views import generic
from django.shortcuts import get_object_or_404, render, redirect
from django.http.response import JsonResponse
from django.db.models.aggregates import Avg

from .models import Product, Category, Review
from .forms import ReviewForm


class HomeListView(generic.ListView):
    template_name = 'main/homelist.html'
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(average_rating=Avg('reviews__rating'))
        queryset = queryset.order_by('-average_rating')
        return queryset


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
        context['average_rating'] = Review.objects.filter(product=self.object).aggregate(Avg('rating'))['rating__avg']
        return context


class AddReviewView(generic.CreateView):
    form_class = ReviewForm
    template_name = 'main/product_detail.html'
    
    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            return JsonResponse({'status': 'error', 'message': 'You need to login or register in order to leave a review.'})

        form.instance.user = self.request.user
        product = get_object_or_404(Product, slug=self.kwargs['slug'])
        form.instance.product = product

        if Review.objects.filter(user=self.request.user, product=product).exists():
            return JsonResponse({'status': 'error', 'message': 'Извините, вы не можете добавить второй отзыв к одному и тому же продукту.'})
        
        review = form.save()
        return JsonResponse({'status': 'success', 'username': review.user.username, 'content': review.review})

           
            # '''С перезагрузкой старницы'''
            # context = {
            #     'form': form,
            #     'product': product,
            #     "error_message": '''Извините, вы не можете добавить второй отзыв к одному и тому же продукту. 
            #     Но вы можете изменить существующий отзыв или удалить его!'''
            # }
            # return render(self.request, self.template_name, context)
        
        # return super().form_valid(form)

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')
    

class DeleteReviewView(generic.DeleteView):
    model = Review
    template_name = 'main/product_detail.html'

    def get_object(self):
        review_id = self.kwargs.get('review_id')
        return get_object_or_404(Review, id=review_id)

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')
    

class UpdateReviewView(generic.UpdateView):
    model = Review
    template_name = 'main/update_review.html'
    fields = ['review', 'rating']

    def get_object(self):
        review_id = self.kwargs.get('review_id')                                                                                                
        return get_object_or_404(Review, id=review_id)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')