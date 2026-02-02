
from django.views import generic
from .models import Product
# Create your views here.

class IndexView(generic.ListView):
    template_name = "mercadinho/index.html"
    context_object_name = "products_label"

    def get_queryset(self):
        return Product.objects.all()
    
    

class DetailView(generic.DetailView):
    model = Product