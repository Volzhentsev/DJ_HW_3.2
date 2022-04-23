from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['title']
    search_fields = ['title', 'description']



class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['address']
    search_fields = ['products']

    def get_queryset(self):
        queryset = Stock.objects.all()
        product = self.request.query_params.get('products')
        if product is not None:
            if product.isdigit():
                queryset = queryset.filter(products=product)
            else:
                queryset = queryset.filter(products__title__icontains=product)

        return queryset

