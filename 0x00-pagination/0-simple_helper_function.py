#!/usr/bin/env python3

"""
Takes two int arg page and page_size
"""


def index_range(page, page_size):
    """
    The function should return a tuple
    """

    start = (page - 1) * page_size
    end = page * page_size
    range_tuple = (start, end)
    return range_tuple
