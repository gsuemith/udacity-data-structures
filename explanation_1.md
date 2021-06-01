I implemented the cache itself as a dictionary and implemented a queue to keep
track of the usage order.  The get and set functions updated the queue as
appropriate.

The use of a list for the queue made both get and set run at O(n).  This could
have been a linked list but that would still be O(n)
