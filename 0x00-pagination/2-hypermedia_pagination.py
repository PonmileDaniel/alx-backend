#!/usr/bin/env python3

"""
Takes two int arg page and page_size
"""
import csv
import math
from typing import List, Dict, Any


def index_range(page, page_size):
    """
    The function should return a tuple
    """

    start = (page - 1) * page_size
    end = page * page_size
    range_tuple = (start, end)
    return range_tuple


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Method that returns desire page
        """
        assert isinstance(page_size, int) and page_size > 0
        assert isinstance(page, int) and page > 0
        datasetlen = len(self.dataset())
        start, end = index_range(page, page_size)
        if start >= datasetlen:
            return []

        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Get hyper method
        """
        assert isinstance(page_size, int) and page_size > 0
        assert isinstance(page, int) and page > 0
        retrieved = self.get_page(page, page_size)
        total_pages = len(retrieved) / page_size
        total_pages = math.ceil(total_pages)

        hyper_data = {
            "page_size": len(retrieved),
            "page": page,
            "data": retrieved,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page + 1 if page > 1 else None,
            "total_pages": total_pages,
        }

        return hyper_data
