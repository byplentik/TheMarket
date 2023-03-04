from django.views import generic


class ProfileTemplateView(generic.TemplateView):
    template_name = 'account/profile.html'