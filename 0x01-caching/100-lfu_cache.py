#!/usr/bin/env python3
""" LFUCache module: LFU caching system. """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache is a caching system using LFU algorithm. """
    def __init__(self):
        """ Initialize """
        super().__init__()
        self.freq = {}
        self.order = []

    def put(self, key, item):
        """
        Add an item in the cache.
        Discard least frequently used if over limit.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.freq[key] += 1
                self.order.remove(key)
            else:
                self.freq[key] = 1
            self.order.append(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                min_freq = min(self.freq.values())
                candidates = [
                    k for k in self.order if self.freq[k] == min_freq
                    ]
                discard = candidates[0]
                self.order.remove(discard)
                del self.cache_data[discard]
                del self.freq[discard]
                print("DISCARD:", discard)

    def get(self, key):
        """ Get an item by key and update frequency. """
        if key is None or key not in self.cache_data:
            return None
        self.freq[key] += 1
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
