from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from my_app.models import Product, Category
from my_app.serializers import ProdSerializer, ProductSerializer#, CategorySerializer


@api_view(['GET', 'POST'])
def get_product(request):
    if request.method == 'POST':
        prod = request.data
        # print(prod)
        prod_ser = ProdSerializer(data=prod)
        if prod_ser.is_valid(raise_exception=True):
            Product.objects.create(**prod_ser.validated_data)

            # print(prod_ser.validated_data)
        # else:
        #     print(prod_ser.errors)
        return Response({"post": prod_ser.data})
    products = Product.objects.all()
    prod_ser = ProductSerializer(products, many=True)
    return Response(prod_ser.data)


@api_view(['PUT', 'DELETE'])
def update_product(request, *args, **kwargs):
    id = kwargs.get('id', None)
    if not id:
        return Response({"errors": "метод обновить не возможен"})
    try:
        product = Product.objects.get(id=id)
    except:
        return Response({"errors": "Объект не найден"})
    if request.method == 'PUT':
        product_serial = ProdSerializer(data=request.data)
        if product_serial.is_valid(raise_exception=True):
            product.title = product_serial.validated_data.get('title')
            product.description = product_serial.validated_data.get('description')
            product.price = product_serial.validated_data.get('price')
            product.category_id = product_serial.validated_data.get('category_id')
            product.save()
        return Response(product_serial.data)
    if request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def get_category(request):
#     cat = Category.objects.all()
#     cat_ser = CategorySerializer(cat, many=True)
#     return Response(cat_ser.data)
