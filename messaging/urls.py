from django.urls import path
from .views import home, list_products
from .views import PublisherListView
from django.views.decorators.cache import cache_page
urlpatterns = [
    path('', home, name="home-page"),
    path('products/', list_products, name="list_products"),
    path('publisher/', PublisherListView.as_view()),
]
