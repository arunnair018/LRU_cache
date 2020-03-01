import logging
logging.basicConfig(level=logging.INFO)

# node structure
class Node:
    def __init__(self,key,val):
        self.key = key  
        self.val = val
        self.next = None
        self.prev = None

# Linked list class
class lru_cache:
    def __init__(self,func):
        self.head = None    # initialize head of list        
        self.tail = None    # initialize tail of list
        self.func = func    
        self.cache={}       # initialize cache 
        self.limit=4        # initialize cache size 

    # function to push into the list
    def _push(self,node):
        if self.head is None:       # if list is empty
            self.head = node
        else:                       # if ist is not empty
            self.tail.next=node 
            node.prev = self.tail
        self.tail=node              # increment tail pointer

    # function to pop the element from list
    def _pop(self,node):
        if node.prev:                       # if node points to previous node
            node.prev.next = node.next       
        else:                               
            self.head = node.next           
        if node.next:                       # if node points to next node
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.next,node.prev = None,None     # make previous and next None

    def __call__(self,*args):
        logging.info('cache_keys : %s', list(self.cache.keys()))   # uncomment to print cache
        self._print(self.head)                     # uncomment to print linked_list
        if args in self.cache:                      # if value in cache then update cache
            n=args[0]
            print(f'Computing...{n}x{n}')
            self._pop(self.cache[args])                 # pop the value
            self._push(self.cache[args])                # push again to update the linked_list with most recently used
            print('from cache : ',end=' ')
            return self.cache[args].val                 # return the value from cache
        else:                                       # if value not in cache
            if len(self.cache) >= self.limit:           # if cache is full
                del self.cache[self.head.key]           # del node reference from cache
                self._pop(self.head)                    # pop node from linked_list

            result = self.func(*args)               # if cache is not filled and new value comes, call function 
            node = Node(args,result)                # store the key and value in node
            self._push(node)                        # push the node into linked_list
            self.cache[args]=node                   # store the reference to node into cache
            return result                           # return cacuated value

    # function to print linked_list
    def _print(self,pointer):
        l=''                     
        while pointer is not None:
            l+= str(pointer.key) + '-->' 
            pointer = pointer.next
        logging.info('linkedlist : %s',l)
