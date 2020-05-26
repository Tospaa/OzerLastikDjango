import pickle
import re

from django.utils import timezone

import api


"""
Here lies my static methods.
Hence the name, methodpack.
"""


def find_ancestor(value, iterable_instance):
    """
    This one is used for finding the ancestor of the given
    value from a Django choices list.
    """
    for i in iterable_instance:
        for j in i[1][0]:
            if j == value:
                return i[0]
    return None


def sorting_key(string_input):
    """
    This one is used for sorting the data by the package
    types right before writing it to the database
    """
    return float(string_input.replace('/', '.'))


def validate_package_type(text):
    stripped_text = ''.join([i for i in re.findall('[0-9/]+', text)])
    if stripped_text and re.match(r'^[1-9][0-9]?(?:/[1-9][0-9]?)?$', stripped_text):
        # d0ru
        return stripped_text
    else:
        raise ValueError(
            f'Provided package type ({stripped_text}) is incorrect.')


def first_class_percentage(instance):
    """
    This one is used for calculating first class percentage.
    Used in home page view.
    """
    first_class_sum = 0
    second_class_sum = 0

    sum_of_packages = 0

    for i in vars(instance).values():
        try:
            data = pickle.loads(i)  # if binary value is empty, raises exception EOFError
                                    # if the value is not binary type, raises TypeError

            if '1' in data.keys():
                for j in data['1'].values():
                    for ic_adet, koli_adet in j.items():
                        first_class_sum += ic_adet*koli_adet
                        sum_of_packages += koli_adet
            if '2' in data.keys():
                for j in data['2'].values():
                    for ic_adet, koli_adet in j.items():
                        second_class_sum += ic_adet*koli_adet
                        sum_of_packages += koli_adet

        except (EOFError, TypeError):
            continue

    return '{:.1f}'.format((first_class_sum/(first_class_sum+second_class_sum))*100), first_class_sum, second_class_sum, sum_of_packages


def monthly_production_and_sales(month_int):
    """
    You feed this method with an int ranging 1-12,
    and it gives you the production and sales data
    of that month. Brilliant.
    """
    if month_int < 1 or month_int > 12:
        raise ValueError(f'Month value ({month_int}) can\'t be out of the 1-12 range.')

    year_int = timezone.localtime(timezone.now()).year

    if month_int > timezone.localtime(timezone.now()).month:
        year_int-=1

    querySet = api.models.KoliDegisiklik.objects.filter(tarih__year=year_int).filter(tarih__month=month_int)

    last_month_production, last_month_sales = 0, 0

    for entry in querySet:
        if entry.koli_adet < 0:
            last_month_sales += entry.koli_adet * entry.kolideki_mamul_adet
        if entry.koli_adet > 0:
            last_month_production += entry.koli_adet * entry.kolideki_mamul_adet

    last_month_sales *= -1

    return last_month_production, last_month_sales
