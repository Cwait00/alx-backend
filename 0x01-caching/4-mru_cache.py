#!/usr/bin/env python3
"""
MRUCache module implementing a Most Recently Used (MRU) caching system.
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching
    and implements an MRU caching system.
    """

    def __init__(self):
        """
        Initialize the MRUCache class.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item to the cache using the MRU algorithm.

        Args:
            key (str): The key of the item.
            item (Any): The item to be stored in the cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            most_recently_used_key = self.order.pop()
            del self.cache_data[most_recently_used_key]
            print(f"DISCARD: {most_recently_used_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            Any: The item associated with the key,
            or None if the key is not found.
        """
        if key is None or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
