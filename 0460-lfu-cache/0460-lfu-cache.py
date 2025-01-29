class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.cnt = 1  # Frequency count
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_front(self, node):
        """Add a node right after head (front of the list)."""
        temp = self.head.next
        node.next = temp
        node.prev = self.head
        self.head.next = node
        temp.prev = node
        self.size += 1

    def remove_node(self, node):
        """Remove a node from the list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1

class LFUCache:
    def __init__(self, capacity: int):
        self.max_size = capacity
        self.min_freq = 0
        self.cur_size = 0
        self.key_node = {}  # Maps key -> Node
        self.freq_list_map = {}  # Maps frequency -> DoublyLinkedList

    def update_freq_list(self, node):
        """Update the frequency of a node and move it to the next frequency list."""
        key = node.key
        self.key_node.pop(key)

        # Remove node from current frequency list
        self.freq_list_map[node.cnt].remove_node(node)
        if node.cnt == self.min_freq and self.freq_list_map[node.cnt].size == 0:
            self.min_freq += 1  # If no nodes left in min_freq, increment

        # Move node to next higher frequency list
        node.cnt += 1
        if node.cnt not in self.freq_list_map:
            self.freq_list_map[node.cnt] = DoublyLinkedList()
        self.freq_list_map[node.cnt].add_front(node)
        self.key_node[key] = node

    def get(self, key: int) -> int:
        """Retrieve a value from the cache and update its frequency."""
        if key in self.key_node:
            node = self.key_node[key]
            self.update_freq_list(node)
            return node.value
        return -1

    def put(self, key: int, value: int):
        """Insert or update a key-value pair in the LFU cache."""
        if self.max_size == 0:
            return  # If capacity is 0, no caching is possible

        if key in self.key_node:
            node = self.key_node[key]
            node.value = value  # Update value
            self.update_freq_list(node)
        else:
            if self.cur_size == self.max_size:
                # Evict the least frequently used node
                min_freq_list = self.freq_list_map[self.min_freq]
                evict_node = min_freq_list.tail.prev  # Least recently used node in min frequency list
                self.key_node.pop(evict_node.key)
                min_freq_list.remove_node(evict_node)
                self.cur_size -= 1

            # Insert new node
            self.cur_size += 1
            self.min_freq = 1
            new_node = Node(key, value)

            if self.min_freq not in self.freq_list_map:
                self.freq_list_map[self.min_freq] = DoublyLinkedList()
            self.freq_list_map[self.min_freq].add_front(new_node)
            self.key_node[key] = new_node
