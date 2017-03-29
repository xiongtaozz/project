from django import template
from datetime import datetime

register = template.Library()

class Translate(template.Node):
	"""docstring for Translate"""
	def __init__(self, format_string):
		super(Translate, self).__init__()
		self.format_string = format_string

	def render(self, context):
		pass

@register.filter(name='translateGermans')
@register.filter(is_safe=False)
def translateGermans(value):
	return value.replace('e', 'a')

@register.simple_tag(takes_context=True)
def get_current_time(context, format_string):
	print(context)
	return datetime.now().strftime(format_string)
