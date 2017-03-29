from jinja2 import Environment, FileSystemLoader, PackageLoader, ChoiceLoader, contextfilter
# from cls3.templatetags.cls3_filter import lower, mycut
import settings
# import os

loader = ChoiceLoader([
        # FileSystemLoader(settings.TEMPLATE_DIRS),
        PackageLoader('lianxi.cls3', 'templates'),
    ])

@contextfilter
def lower(value):
	return value.lower()

# env = Environment()
# # env.filters['mycut'] = mycut
# env.filters['my_lower'] = lower

