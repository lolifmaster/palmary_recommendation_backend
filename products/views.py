from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.filters import SearchFilter

from products.models import Product, Category, Type
from products.serializer import ProductSerializer, CategorySerializer, TypeSerializer
from products.pagination import CustomCursorPagination


class ProductView(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomCursorPagination
    lookup_field = 'id'
    filter_backends = [SearchFilter]
    search_fields = ['name', 'category__name', 'type__name']


class CategoryView(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TypeView(ReadOnlyModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer()
