import django_filters
from django_filters import DateFilter, CharFilter

from product.models import *

class ProductFilter(django_filters.FilterSet):
	title = CharFilter(field_name='title', lookup_expr='icontains')
	var = CharFilter(field_name='product_variant_one', lookup_expr='icontains')
	price = CharFilter(field_name='price', lookup_expr='icontains')
	start_date = DateFilter(field_name="date_created", lookup_expr='year')

	class Meta:
		model = ProductVariantPrice
		fields = ['title','price','start_date']
		