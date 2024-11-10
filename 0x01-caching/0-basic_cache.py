#!/usr/bin/env python3

""" This module defines a class BasicCache
"""
BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """ BasicCache class that inherits from BaseCaching and is a caching system
        without any limit.
    """
    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key from the cache_data dictionary
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
