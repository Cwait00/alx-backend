#!/usr/bin/env python3
"""
LFUCache module implementing a Least Frequently Used (LFU) caching system.
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching and
    implements an LFU caching system.
    """

    def __init__(self):
        """
        Initialize the LFUCache class.
        """
        super().__init__()
        self.freq = {}
        self.usage_order = []

    def put(self, key, item):
        """
        Add an item to the cache using the LFU algorithm.

        Args:
            key (str): The key of the item.
            item (Any): The item to be stored in the cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used item
                lfu_key = min(
                    self.freq,
                    key=lambda k: (self.freq[k], self.usage_order.index(k))
                )
                self.cache_data.pop(lfu_key)
                self.freq.pop(lfu_key)
                self.usage_order.remove(lfu_key)
                print(f"DISCARD: {lfu_key}")

            self.cache_data[key] = item
            self.freq[key] = 1
            self.usage_order.append(key)

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

        self.freq[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]

    def print_cache(self):
        """
        Print the current state of the cache.
        """
        print("Current cache:")
        for key, value in self.cache_data.items():
            print(f"{key}: {value}")
