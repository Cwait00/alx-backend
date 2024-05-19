#!/usr/bin/env python3
"""
Hypermedia pagination
"""

from typing import List, Tuple, Union, Optional
import csv
import math


# Function to calculate index range
def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.

    Args:
        page (int): Current page number (1-indexed).
        page_size (int): Number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing start index and end index.
    """
    start_idx = (page - 1) * page_size
    end_idx = page * page_size
    return start_idx, end_idx


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List[str]]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        Get a page of data from the dataset.

        Args:
            page (int): Current page number (1-indexed). Default is 1.
            page_size (int): Number of items per page. Default is 10.

        Returns:
            List[List[str]]: List of rows corresponding to the page.
        """
        assert isinstance(page, int) and page > 0, \
            "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be a positive integer"

        dataset = self.dataset()
        start_idx, end_idx = index_range(page, page_size)
        if start_idx >= len(dataset):
            return []  # Return an empty list if start_idx is out of range

        return dataset[start_idx:end_idx]

    def get_hyper(
        self,
        page: int = 1,
        page_size: int = 10
    ) -> dict:
        """
        Get hypermedia pagination details for a page of data.

        Args:
            page (int): Current page number (1-indexed). Default is 1.
            page_size (int): Number of items per page. Default is 10.

        Returns:
            dict: Pagination details.
        """
        assert isinstance(page, int) and page > 0, \
            "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be a positive integer"

        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }


# Testing the implementation
if __name__ == "__main__":
    server = Server()

    print(server.get_hyper(1, 2))
    print("---")
    print(server.get_hyper(2, 2))
    print("---")
    print(server.get_hyper(100, 3))
    print("---")
    print(server.get_hyper(3000, 100))
