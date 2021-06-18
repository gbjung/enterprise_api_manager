from django.urls import include, path
from . import views


from .views import HomePageView, SearchAllView, SearchResultView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('index.html', HomePageView.as_view(), name='home'),
    path('search-all', SearchAllView.as_view(), name='search-all'),
    path('search-results', SearchResultView.as_view(), name='search_result')
]
