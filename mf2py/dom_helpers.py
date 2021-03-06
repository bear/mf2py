import sys
if sys.version < '3':
    text_type = unicode
    binary_type = str
else:
    text_type = str
    binary_type = bytes


def get_attr(el, attr, check_name=None ):
    """returns the attribute of an element if it exists and is not empty else returns None. Optional kwarg 'check_name' (as a list of strings or single string) to check element type by name
    """
    if check_name is None:
        attr_value = el.get(attr, None)
    elif el.name in check_name:
        attr_value = el.get(attr, None)
    else:
        attr_value = None

    if isinstance(attr_value, text_type) or isinstance(attr_value, binary_type):
        if attr_value.strip() == "":
            attr_value = None

    return attr_value
