class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity if capacity != MIN_CAPACITY else capacity
        self.table = [None] * self.capacity
        self.size = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.elements / self.get_num_slots()

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        hashed = 14695981039346656037
        for c in key:
            hashed *= 1099511628211
            hashed = hashed ^ ord(c)
            hashed &= 0xffffffffffffffff
        return hashed

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hashed = 5381
        for c in key:
            hashed = hashed * 33 + ord(c)
            hashed &= 0xffffffff
        return hashed

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        entry = self.table[index]
        if not entry:
            self.size += 1
            self.table[index] = HashTableEntry(key, value)
        else:
            if entry.key == key:
                self.table[index] = HashTableEntry(key, value)
            while entry.next:
                if entry.key == key:
                    return
                entry = entry.next
            self.size += 1
            entry.next = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if not self.table[index]:
            print(f"{key} not found")
        else:
            previous_entry = None
            entry = self.table[index]
            if not entry.next:
                self.size -= 1
                self.table[index] = None
                return entry.value
            while entry:
                if entry.key == key:
                    if not previous_entry and entry.next:
                        self.size -= 1
                        self.table[index] = entry.next
                        return entry.value
                    else:
                        self.size -= 1
                        previous_entry.next = entry.next
                previous_entry = entry
                entry = entry.next
            print(f"{key} not found")

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if not self.table[index]:
            return
        else:
            entry = self.table[index]
            while entry:
                if entry.key == key:
                    return entry.value
                entry = entry.next
            return

    def resize(self, new_cap):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        self.capacity = int(new_cap)
        old = self.table
        self.table = [None] * self.capacity
        for element in old:
            current = element
            if element is not None:
                self.put(element.key, element.value)
                while current.next is not None:
                    current = current.next
                    self.put(current.key, current.value)


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
