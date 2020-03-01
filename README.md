# LRU Cache
Python implementation of Least Recently Used Cache (LRU Cache) using dict and linked list.
* Least Recently Used Cache.
* Evicts least recently used entry.
* Uses double linked list and dictionary.

Some of the requirements to implement lru cache:
1. Fixed size: bound to limited memory usage.
2. Fast access: insertion and retrieval should be in O(1) time complexity.
3. Entry replacement when cachelimit reaches: efficiently evict the entry when memory limit reaches.

## How to use
* clone **LRU_cache.py** file into the working directory.
* import the class **from LRU_cache import lru_cache**.
* set **lru_cache.limit**.
* use the wrapper **@LRUCache** before the function.

## Testing
To test and see how linked list and dictionary are populating, uncomment **logging.basicConfig(level=logging.INFO)**.

## Built with
**Python 3.7.3**.
