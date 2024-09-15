# src/utils/helpers.py
from functools import lru_cache

@lru_cache(maxsize=None)
def cached_function(func):
    return func
