from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('produtos', views.ProdutoListView.as_view(), name='produtos'),
    path('produtos/<int:tipo_id>/', views.ProdutoPorTipoListView.as_view(), name='produtos'),
]
