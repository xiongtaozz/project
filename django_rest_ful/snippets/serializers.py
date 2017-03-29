from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet
# from django.db import models
from snippets import models


# class SnippetSerializer(serializers.ModelSerializer):
#     # pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
#     # title = serializers.CharField(required=False,
#     #                               max_length=100)
#     # code = serializers.CharField(max_length=100000)
#     # linenos = serializers.BooleanField(required=False)
#     # language = serializers.ChoiceField(choices=models.LANGUAGE_CHOICES,
#     #                                    default='python')
#     # style = serializers.ChoiceField(choices=models.STYLE_CHOICES,
#     #                                 default='friendly')
#     #
#     # def restore_object(self, attrs, instance=None):
#     #     """
#     #     Create or update a new snippet instance.
#     #     """
#     #     if instance:
#     #         # Update existing instance
#     #         instance.title = attrs['title']
#     #         instance.code = attrs['code']
#     #         instance.linenos = attrs['linenos']
#     #         instance.language = attrs['language']
#     #         instance.style = attrs['style']
#     #         return instance
#     #
#     #     # Create new instance
#     #     return Snippet(**attrs)
#     class Meta:
#         model = Snippet
#         fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

