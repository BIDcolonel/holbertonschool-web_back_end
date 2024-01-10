#!/usr/bin/env python3
""" Pagination project, helper function module """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns the start and end indices corresponding to a given page and
    page size.

    Args:
    - page (int): The page number (1-indexed).
    - page_size (int): The number of items per page.

    Returns:
    - tuple[int, int]: A tuple containing the start and end indices for the
    given page and page size."""
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return start_index, end_index
