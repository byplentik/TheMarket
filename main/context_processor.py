from .models import Category

def display_categories(request):
    cats = Category.objects.all()
    return {'cats': cats}