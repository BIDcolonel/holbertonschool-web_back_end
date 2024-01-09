#!/usr/bin/env python3
"""Hypermedia pagination module"""
import csv
import math
from typing import List
from typing import Tuple


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """Returns the start and end indices corresponding to a given page and
    page size.

    Args:
    - page (int): The page number (1-indexed).
    - page_size (int): The number of items per page.

    Returns:
    - tuple[int, int]: A tuple containing the start and end indices for the
    given page and page size."""
    if not isinstance(page, int) or not isinstance(page_size, int) or \
    page <= 0 or page_size <= 0:
        raise ValueError("Page and page_size must be positive integers.")

    start_index = (page - 1) * page_size
    end_index = page * page_size

    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Method that stores the dataset in a list instance attribute named"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Method that takes two integer arguments page with default value 1"""
        self.dataset()
        for i in [page, page_size]:
            assert isinstance(i, int) and page > 0
        assert page_size > 0
        range_i = index_range(page, page_size)
        return self.__dataset[range_i[0]:range_i[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Get hypermedia pagination.

            Args:
            - page: page number.
            - page_size: number of items per page.

            Return:
            - A dictionary."""
        data: int = self.get_page(page, page_size)
        totalPages: int = math.ceil(len(self.__dataset) / page_size)
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if (page + 1) <= totalPages else None,
            'prev_page': page - 1 if (page - 1) > 0 else None,
            'total_pages': totalPages
        }
