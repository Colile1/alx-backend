#!/usr/bin/env python3
""" FIFOCache module: FIFO caching system. """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache is a caching system using FIFO algorithm. """
    def __init__(self):
        """ Initialize """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache. Discard first if over limit. """
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.order.append(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discard = self.order.pop(0)
                del self.cache_data[discard]
                print("DISCARD:", discard)

    def get(self, key):
        """ Get an item by key. """
        if key is None:
            return None
        return self.cache_data.get(key, None)
