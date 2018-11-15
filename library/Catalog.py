# CLASS VIEWS
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = "catalogue.html"


class Catalogue(TemplateView):
    template_name = "catalogue.html"
