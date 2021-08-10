from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Product

class ProductSerializer(ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='product-details', read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'imageUrl',
            # 'url'

        ]
