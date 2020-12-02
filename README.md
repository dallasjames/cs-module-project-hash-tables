# Hash Tables

## Day 1
Implemented a `HashTable` class and `HashTableEntry` class
Implemented a DJB2 hashing function
Implemented the `hash_index()` that returns an index value for a key.
Implemented the `put()`, `get()`, and `delete()` methods.
Tested with:
```
python test_hashtable_no_collisions.py
```
## Day 2
Implemented linked-list chaining for collision resolution
Modified `put()`, `get()`, and `delete()` methods to handle collisions
Tested with:
```
python test_hashtable.py
```
Implemented load factor measurements and automatic hashtable size
doubling.
Compute and maintain load factor.
When load factor increases above `0.7`, automatically rehash the
table to double its previous size.
Add the `resize()` method.
Tested with:
```
python test_hashtable.py
python test_hashtable_resize.py
```
