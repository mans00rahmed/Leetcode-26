# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 21:33:04 2026

@author: mans00rahmed
"""


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}      # key -> value
        self.counter = {}    # key -> "recency" count

    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache[key]
            self.counter[key] = self.get_max_count() + 1
            return value
        return -1
    
    def get_max_count(self):
        return max(self.counter.values()) if self.counter else 0

    def put(self, key: int, value: int) -> None:
        if key in self.cache and key in self.counter:
            self.cache[key] = value
           
            self.counter[key] = self.get_max_count() + 1
        else:
            if len(self.cache) < self.capacity:
                self.cache[key] = value
                self.counter[key] = self.get_max_count() + 1

            else:
                evict_key = min(self.counter, key=self.counter.get)
                del self.cache[evict_key]
                del self.counter[evict_key]
                self.cache[key] = value
                self.counter[key] = self.get_max_count() + 1