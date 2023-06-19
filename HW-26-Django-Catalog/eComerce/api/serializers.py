from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        main_image = obj.productimage_set.filter(is_main=True).first()
        if main_image:
            return main_image.photo_encoded
        return None

    class Meta:
        model = Product
        fields = ["id", "title", "description", "price", "discount_price", "image"]
