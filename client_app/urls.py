from django.urls import include, path
from . import views


from .views import (HomePageView, SearchAllView, SearchResultView,
                   TaxSearchHomeView, TaxSearchGetStartedView, TaxSearchReferenceView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('search-all', SearchAllView.as_view(), name='search-all'),
    path('search-results', SearchResultView.as_view(), name='search_result'),
    path('tax-search-home', TaxSearchHomeView.as_view(), name='tax-search-home'),
    path('tax-search-get-started', TaxSearchGetStartedView.as_view(), name='tax-search-get-started'),
    path('tax-search-reference-docs', TaxSearchReferenceView.as_view(), name='tax-search-reference-docs'),
    path('tax-search-release-notes', TaxSearchGetStartedView.as_view(), name='tax-search-release-notes')
]
