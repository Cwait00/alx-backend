#!/usr/bin/env python3
""" LFUCache module
"""

from base_caching import BaseCaching
from collections import defaultdict
import time


class LFUCache(BaseCaching):
    """ LFUCache class
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.usage_count = {}
        self.frequency = defaultdict(list)
        self.last_used = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_count[key] += 1
        else:
            self.cache_data[key] = item
            self.usage_count[key] = 1

        self.update_frequency(key)
        self.last_used[key] = time.time()

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.evict()

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.usage_count[key] += 1
            self.update_frequency(key)
            self.last_used[key] = time.time()
            return self.cache_data[key]
        else:
            return None

    def update_frequency(self, key):
        """ Update frequency dictionary
        """
        count = self.usage_count[key]
        if count - 1 in self.frequency:
            self.frequency[count - 1].remove(key)
            if not self.frequency[count - 1]:
                del self.frequency[count - 1]

        self.frequency[count].append(key)

    def evict(self):
        """ Evict least frequency used item
        """
        min_frequency = min(self.frequency)
        keys_to_evict = self.frequency[min_frequency]

        if len(keys_to_evict) > 1:

            least_recently_used = min(
                keys_to_evict,
                key=lambda k: self.last_used[k]
            )
            keys_to_evict.remove(least_recently_used)
        else:
            least_recently_used = keys_to_evict.pop(0)

        del self.cache_data[least_recently_used]
        del self.usage_count[least_recently_used]
        del self.last_used[least_recently_used]

        if not self.frequency[min_frequency]:
            del self.frequency[min_frequency]

        print(f"DISCARD: {least_recently_used}")
