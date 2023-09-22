import os

from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.translation import gettext_lazy as _

from products.models import Product, Category, Type
from products.serializer import ProductSerializer, CategorySerializer, TypeSerializer
from products.pagination import CustomCursorPagination


class ProductView(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomCursorPagination
    lookup_field = 'id'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['category__name', 'type__name']
    search_fields = ['name', 'category__name', 'type__name']

    @action(detail=False, methods=['post'], description=_('Get recommendation based on 3 selected products'), url_path='recommendation')
    def get_recommendation(self, request):
        selected_products = request.data.get('products')
        if len(selected_products) != 3:
            return Response({'message': _('Please select 3 products')}, status=status.HTTP_400_BAD_REQUEST)
        try:
            products = Product.objects.filter(id__in=selected_products)
            if len(products) != 3:
                return Response({'message': _('Please select 3 products')}, status=status.HTTP_400_BAD_REQUEST)
            pwd = os.path.dirname(__file__)
            # save these products into a row in csv file
            with open('static/products.csv', 'a+') as file:
                file.write(f'{products[0].id},{products[1].id},{products[2].id}\n')
            category = products[0].category
            type = products[0].type
            recommendation = Product.objects.filter(category=category, type=type).exclude(id__in=selected_products)
            serializer = self.get_serializer(recommendation, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': _('Please select 3 products from out catalog')}, status=status.HTTP_400_BAD_REQUEST)


class CategoryView(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TypeView(ReadOnlyModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
