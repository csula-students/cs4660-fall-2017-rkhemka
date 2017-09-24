"""dsdsaLists defines simple list related operations"""

from __future__ import division

def get_first_item(li):
    
    return li[0]

def get_last_item(li):
    """Return the last item from the list"""
    return li[-1];


def get_second_and_third_items(li):
    """Returzn second and third item from the list"""
    return li[1:3]

def get_sum(li):
    """Return the sum of the list items"""
    return sum(li)

def get_avg(li):
    avg = float(sum(li)/len(li))
    return avg
    """Returns the average of the list items"""