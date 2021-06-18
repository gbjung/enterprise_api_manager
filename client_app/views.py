from django.http import HttpResponse
from django.template import loader
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class SearchAllView(TemplateView):

    template_name = "search-all.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class SearchResultView(TemplateView):

    template_name = "search-api-results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
