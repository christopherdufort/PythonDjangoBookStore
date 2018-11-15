# CLASS VIEWS
from django.views.generic import TemplateView

class Catalogue(TemplateView):
    template_name = "catalogue.html"
