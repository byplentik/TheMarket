from django.views import generic

from .forms import CustomUserChangeForm

class ProfileTemplateView(generic.FormView):
    template_name = 'account/profile.html'
    form_class = CustomUserChangeForm

    def get_object(self):
        return self.request.user
    
    def get_success_url(self) -> str:
        return self.request.META.get('HTTP_REFERER')

    def form_valid(self, form):
        user = self.request.user
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.save()
        return super().form_valid(form)
    