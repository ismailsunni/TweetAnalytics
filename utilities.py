# utilities function
# author : @ismailsunni
# contact : imajimatika@gmail.com
# created : 27/02/2012

import operator

def sort_dict(my_dict, num_elements=-1, descending=True):
    """Sort dictionary by the value and return the first num_elements
    """
    retval = sorted(my_dict.iteritems(), key=operator.itemgetter(1),
            reverse=descending)
    num_retrieve = 0
    if num_elements >= len(my_dict) or num_elements < 0:
        num_retrieve = len(my_dict)
    else:
        num_retrieve = num_elements
    return retval[:num_retrieve]