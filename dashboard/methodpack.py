import re

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
