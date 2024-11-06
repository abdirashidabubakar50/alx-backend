#!/usr/bin/env python3
"""

This script defines a function called index_range that takes two arguments page and page_size

"""

def index_range(page: int, page_size: int) -> tuple:
    """
    This function takes two integer arguments and returns a tuple of size two
    containing a start index and an end index corrresponding to the range of indexes
    to return in a list or those particular pagination parameters

    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)