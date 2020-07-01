import os
import pickle
import re

from django.conf import settings
from django.utils import timezone
from PIL import Image

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


def koli_son_durum_iterator(instance):
    """
    This one is used for iterating over the given KoliSonDurum object.
    Used in home page view.
    Used for calculating:
    - first class percentage,
    - first class pairs sum,
    - second class pairs sum,
    - sum of all packages
    and returns values respectively.
    """
    if type(instance) != api.models.KoliSonDurum:
        raise ValueError("Type of instance ({}) is not appropriate for koli_son_durum_iterator method.".format(type(instance).__name__))

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


def monthly_production_and_sales(month_int, year_int):
    """
    You feed this method with an int ranging 1-12,
    and a year, of course,
    and it gives you the production and sales data
    of that month. Brilliant.
    """
    if month_int < 1 or month_int > 12:
        raise ValueError(f'Month value ({month_int}) can\'t be out of the 1-12 range.')

    querySet = api.models.KoliDegisiklik.objects.filter(tarih__year=year_int).filter(tarih__month=month_int).filter(imalat=True)

    last_month_production, last_month_sales = 0, 0

    for entry in querySet:
        if entry.koli_adet < 0:
            last_month_sales += entry.koli_adet * entry.kolideki_mamul_adet
        if entry.koli_adet > 0:
            last_month_production += entry.koli_adet * entry.kolideki_mamul_adet

    last_month_sales *= -1

    return last_month_production, last_month_sales


def profile_photo_resizer(rel_photo_addr, crop_box):
    """
    This method resizes the provided photo to
    the standard size, which is 128x128. This
    standard is set by me.
    """
    photo_addr = os.path.join(settings.MEDIA_ROOT, rel_photo_addr)
    Image.open(photo_addr).crop(crop_box).resize((128, 128), Image.BICUBIC).save(photo_addr)


def find_full_name_from_choice(value, iterable_instance):
    """
    This method gives the full name of the given
    choice from Django choice list.
    """
    for i in iterable_instance:
        for j in i[1]:
            if value == j[0]:
                return j[1]
    return None
