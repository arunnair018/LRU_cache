import random
import time
from LRU_cache import lru_cache
lru_cache.limit=5

@lru_cache
def _square(n):
    print(f'Computing...{n}x{n}')
    time.sleep(1)
    return n*n
    
# random input generator
for i in range(20):
    print(_square(random.randrange(1,7)))
    print('---------------------------------')