#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List[str]]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude header row

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List[str]]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
        """
        Get hypermedia pagination with deletion resilience.

        Args:
            index (int): Starting index of the page.
            page_size (int): Number of items per page.

        Returns:
            Dict[str, Any]: Pagination details.
        """
        assert index is not None and isinstance(index, int) and index >= 0
        indexed_data = self.indexed_dataset()
        assert index < len(indexed_data)

        data = []
        next_index = index
        count = 0

        while count < page_size and next_index < len(indexed_data):
            if next_index in indexed_data:
                data.append(indexed_data[next_index])
                count += 1
            next_index += 1

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }


# Testing the implementation
if __name__ == "__main__":
    server = Server()

    print("Testing get_hyper_index...")
    try:
        server.get_hyper_index(300000, 100)
    except AssertionError:
        print("AssertionError raised when out of range")

    index = 3
    page_size = 2

    server.indexed_dataset()

    print("Nb items: {}".format(len(server._Server__indexed_dataset)))

    # 1- request first index
    res = server.get_hyper_index(index, page_size)
    print(res)

    # 2- request next index
    print(server.get_hyper_index(res.get('next_index'), page_size))

    # 3- remove the first index
    del server._Server__indexed_dataset[res.get('index')]
    print("Nb items: {}".format(len(server._Server__indexed_dataset)))

    # 4- request again the initial index -> the first data retrieves
    #    is not the same as the first request
    print(server.get_hyper_index(index, page_size))

    # 5- request again initial next index -> same data page as
    #    the request 2-
    print(server.get_hyper_index(res.get('next_index'), page_size))
