from django.test import TestCase
from django.utils.translation import ugettext as _
# Create your tests here.


def my_view():
    output = _('Welcome to my site.')
    print output

my_view()