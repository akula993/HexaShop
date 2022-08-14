from django.urls import path

from shop.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<slug:slug_category>/', HomeView.as_view(), name='category'),
    path('<slug:slug_product>/', HomeView.as_view(), name='product'),

]
