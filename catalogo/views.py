from django.shortcuts import render
from django.http import HttpResponse
from catalogo.models import Tipo, Produto
from django.utils import timezone
from django.views.generic.list import ListView

def index(request):
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', {'tipos': Tipo.objects.all()})


class ProdutoListView(ListView):
    model = Produto
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['tipos'] = Tipo.objects.all()
        return context

class ProdutoPorTipoListView(ListView):
    model = Produto
    template_name = 'catalogo/produto_list.html'

    def get_queryset(self):
        return Produto.objects.filter(tipo__id=self.kwargs['tipo_id'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['tipos'] = Tipo.objects.all()
        context['tipo_sel'] = Tipo.objects.get(pk=self.kwargs['tipo_id'])
        return context
