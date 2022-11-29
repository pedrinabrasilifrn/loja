from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('produtos', views.ProdutoListView.as_view(), name='produtos'),
]