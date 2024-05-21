#!/usr/bin/env python3
""" MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.usage_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            most_recently_used = self.usage_order.pop()
            del self.cache_data[most_recently_used]
            print(f"DISCARD: {most_recently_used}")

        self.cache_data[key] = item
        self.usage_order.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        else:
            return None

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in self.cache_data:
            print(f"{key}: {self.cache_data[key]}")
