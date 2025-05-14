#!/usr/bin/env python3
""" MRUCache module: MRU caching system. """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache is a caching system using MRU algorithm. """
    def __init__(self):
        """ Initialize """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item in the cache. Discard most recently used if over limit.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            self.order.append(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discard = self.order.pop(-2)
                del self.cache_data[discard]
                print("DISCARD:", discard)

    def get(self, key):
        """ Get an item by key and mark as most recently used. """
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
