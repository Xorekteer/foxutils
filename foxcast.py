def flatten_iterable(to_flatten):
    """ Flatten nested lists and tuples into a non-nested list recursively. """
    res = list()
    def is_list_or_tuple(elem):
        return isinstance(elem, list) or isinstance(elem, tuple) 
    def recursion(to_flatten):
        for elem in to_flatten:
            if is_list_or_tuple(elem):
                recursion(elem)
            else:
                res.append(elem)
    # protect non-list and non-tuple iterables (e.g. string) from being iterated over
    if is_list_or_tuple(to_flatten):    # list or tuple?
        recursion(to_flatten)           # call recursion
    else:
        res.append(to_flatten)  # just return the original
    return res
