#!/usr/bin/env python3
""" 0-Simple helper function"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """Returns the start and end indices corresponding to a given page and
    page size.

    Args:
    - page (int): The page number (1-indexed).
    - page_size (int): The number of items per page.

    Returns:
    - tuple[int, int]: A tuple containing the start and end indices for the
    given page and page size.
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Page and page_size must be positive integers.")

    start_index = (page - 1) * page_size
    end_index = page * page_size

    return start_index, end_index
