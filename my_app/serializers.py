import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

# from my_app.models import Category

#
# class CatSerTest(serializers.Serializer):
#     name = serializers.CharField(max_length=128)
#     description = serializers.CharField()
#
# def encode():
#     model = Category.objects.first()
#     ser_mod = CatSerTest(model)
#     print(ser_mod.data)
#     json = JSONRenderer().render(ser_mod.data)
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"name":"\xd0\xa5\xd0\xbb\xd0\xb5\xd0\xb1\xd0\xbe\xd0\xb1\xd1\x83\xd0\xbb\xd0\xbe\xd1\x87\xd0\xbd\xd1\x8b\xd0\xb5","description":"\xd0\xb8\xd0\xb7\xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb8\xd1\x8f \xd0\xb8\xd0\xb7 \xd1\x85\xd0\xbb\xd0\xb5\xd0\xb1\xd0\xb0"}'
# )
#     json = JSONParser().parse(stream)
#     print(json)
#     ser = CatSerTest(data=json)
#     print(ser)
#     ser.is_valid()
#     print(ser.validated_data)


class ProdSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=128)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    description = serializers.CharField()
    category_id = serializers.IntegerField()
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get("title", validated_data.title)
    #     instance.description = validated_data.get("description", validated_data.description)
    #     instance.price = validated_data.get("price", validated_data.price)
    #     instance.category_id = validated_data.get("category_id", validated_data.category_id)
    #     instance.save()
    #     return instance

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    description = serializers.CharField(max_length=500)
    # product_set = ProdSerializer()
    # product_set = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=128)
    description = serializers.CharField(max_length=128)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    category = CategorySerializer()


