from django import template
import json

register = template.Library()

@register.filter(name='abs')
def abs_filter(value):
    return abs(value)

@register.filter(name='msdjson', is_safe=True)
def mamul_son_durum_json_to_html(value):
    try:
        data = json.loads(value)
        html_form = ''
        for i in data:
            html_form += '<b>{0}</b> numara, <b>{1}</b> çift<br />'.format(i, data[i])
        return html_form[:-6]
    except json.decoder.JSONDecodeError:
        return ''
