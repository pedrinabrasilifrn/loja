from django.shortcuts import render
from django.http import HttpResponse
from catalogo.models import Tipo, Produto
from django.utils import timezone
from django.views.generic.list import ListView

def index(request):

    #return HttpResponse("Hello, world. You're at the polls index.")
    context = {
        
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class ProdutoListView(ListView):
    model = Produto
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
