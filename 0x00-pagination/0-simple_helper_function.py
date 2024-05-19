#!/usr/bin/env python3
"""
Simple helper function for pagination
"""

from typing import Tuple  # Import Tuple from typing module


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.

    Page numbers are 1-indexed, i.e. the first page is page 1.

    Args:
        page (int): Current page number (1-indexed).
        page_size (int): Number of items per page.

    Returns:
        tuple: A tuple containing start index and end index.
    """
    start_idx = (page - 1) * page_size
    end_idx = page * page_size
    return (start_idx, end_idx)


# Testing the function
if __name__ == "__main__":
    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)
