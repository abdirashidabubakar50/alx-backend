#!/usr/bin/env python3
"""

This script defines a function called index_range that takes
two arguments page and page_size

"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    This function takes two integer arguments and returns a tuple of size two
    containing a start index and an end index corrresponding to the range of
    indexes to return in a list or those particular pagination parameters

    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieve the specified page of data
        """

        # page and page_size are both integers and greater than 0
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) > 0

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)

        # Return the requested page or an empty list if out of range
        if start_index < len(dataset):
            return []
        return dataset[start_index:end_index]
