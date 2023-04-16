from .models import Category


def display_categories(request):    
    cats = Category.objects.all()
    if request.user.is_authenticated:
        return {
            'user_absolute_url': request.user.get_absolute_url(),
            'cats': cats,
        }
    
    return {'cats': cats,}