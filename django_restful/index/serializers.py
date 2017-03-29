from rest_framework import viewsets, serializers
from django.contrib.auth.models import User
from models import Product, Tag


class UserSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialize


class ProSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'style', 'qty', 'price', 'city', 'keys', 'remark')


class ProViewsSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProSerializer


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('key')


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

