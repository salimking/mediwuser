from django.views import generic
from product.forms import VariantForm,ProductCreateForm
from django.views.generic import CreateView 
from product.models import Variant,Product,ProductVariant
from django.views.generic import ListView
from product.Pfilter import ProductFilter
from django.views.generic.list import ListView
from django.shortcuts import render
# class CreateProductView(generic.TemplateView):
#     template_name = 'products/create.html'

#     def get_context_data(self, **kwargs):
#         context = super(CreateProductView, self).get_context_data(**kwargs)
#         variants = Variant.objects.filter(active=True).values('id', 'title')
#         context['product'] = True
#         context['variants'] = list(variants.all())
#         return context
class CreateProductView(CreateView):
    form_class = ProductCreateForm
    model = Product
    template_name = 'products/create.html'
    success_url = '/'
    
    # success_url = "/create"
def ProductListView(request):
    product= Product.objects.all()   
    variant= Variant.objects.all()   
    pv= ProductVariant.objects.all()  
      

    s = ProductFilter(request.GET,queryset=pv) 

    context={
        "p":product,
        'v':variant,
        'pv':pv,
        's':s,
    }

    return render(request,'products/list.html',context) 

def search(request):
    pv= ProductVariant.objects.all()   

    s = ProductFilter(request.GET,queryset=pv)
    context={
        "s":s
    }

    return render(request,'products/list.html',context) 

# class ContactListView(ListView):
#     paginate_by = 2
#     model = Contact