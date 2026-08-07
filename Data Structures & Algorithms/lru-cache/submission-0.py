class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None

class LRUCache:
    
    # linked list put or delete 都是 O(1)，但是查找慢
    # array list 查找方便，但是插入删除慢
    # 不一定用 double linked list，可以用 map{key: int key; value: pre node}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = Node()
        self.tail = self.head
    
    def push_back(self, node):
        self.tail.next = node
        self.map[node.key] = self.tail
        self.tail = self.tail.next
    
    def pop_front(self):
        newHead = self.head.next
        self.map.pop(newHead.key)
        self.head = newHead

    def move_to_tail(self, prev):
        curr = prev.next
        if curr == self.tail:
            return
        
        next = curr.next
        if next:
            self.map[next.key] = prev
        
        prev.next = next
        curr.next = None
        self.push_back(curr)

    def get(self, key: int) -> int:
        # type key: int
        # rtype: int
        if key not in self.map:
            return -1
        
        prev = self.map[key]
        val = prev.next.val
        self.move_to_tail(prev)

        return val


        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            prev = self.map[key]
            prev.next.val = value
            self.move_to_tail(prev)
        else:
            newNode = Node(key, value)
            self.push_back(newNode)

            if len(self.map) > self.capacity:
                self.pop_front()
                


        
