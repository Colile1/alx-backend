#!/usr/bin/env python3
""" LRUCache module: LRU caching system. """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache is a caching system using LRU algorithm. """
    def __init__(self):
        """ Initialize """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item in the cache. Discard least recently used if over limit.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            self.order.append(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discard = self.order.pop(0)
                del self.cache_data[discard]
                print("DISCARD:", discard)

    def get(self, key):
        """ Get an item by key and mark as recently used. """
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
