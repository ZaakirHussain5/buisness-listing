from django import template
from listings.models import Category
register = template.Library()

@register.inclusion_tag('pages/partials/header.html', takes_context=True)
def show_categories(context):
    categories = Category.objects.all()
    return {'headerCategories':categories , "request":context["request"]}