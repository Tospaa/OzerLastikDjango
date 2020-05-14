import re
import pickle

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
        raise ValueError(f'Provided package type ({stripped_text}) is incorrect.')

def first_class_percentage(instance):
    first_class_sum = 0
    second_class_sum = 0

    for i in vars(instance).values():
        try:
            data = pickle.loads(i)  # if binary value is empty, raises exception EOFError
                                    # if the value is not binary type, raises TypeError

            if '1' in data.keys():
                for j in data['1'].values():
                    for ic_adet, koli_adet in j.items():
                        first_class_sum+=ic_adet*koli_adet
            if '2' in data.keys():
                for j in data['2'].values():
                    for ic_adet, koli_adet in j.items():
                        second_class_sum+=ic_adet*koli_adet

        except (EOFError, TypeError):
            continue

    return int((first_class_sum/(first_class_sum+second_class_sum))*100)
