
from django.views import generic
from .models import Product
# Create your views here.

class IndexView(generic.ListView):
    
    template_name = "mercadinho/index.html"

    def get_queryset(self):
        return []
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test'] = 'saitama'  # Adicionando a variável ao contexto
        return context

class DetailView(generic.DetailView):
    model = Product