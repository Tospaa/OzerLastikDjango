from django import template
from django.utils.safestring import mark_safe
import pickle

register = template.Library()

@register.filter(name='abs')
def abs_filter(value):
    return abs(value)

@register.filter(name='ksdpackonly')
def koli_son_durum_binary_to_html(value):
    try:
        data = pickle.loads(value)  # if binary value is empty, raises exception EOFError
        html_code = ''

        if '1' in data:
            first_class_prod_sum = 0
            first_class_pack_sum = 0
            for i in data['1'].values():
                for j in i.values():
                    first_class_pack_sum += j
            html_code = f'1. kalite toplam: <b>{first_class_pack_sum}</b> koli'
        if '2' in data:
            second_class_prod_sum = 0
            second_class_pack_sum = 0
            for i in data['2'].values():
                for j in i.values():
                    second_class_pack_sum += j
            if html_code:
                html_code += '<br />'
            html_code += f'2. kalite toplam: <b>{second_class_pack_sum}</b> koli'

        return mark_safe(html_code)
    except EOFError:
        return ''
