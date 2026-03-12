class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.node_num = 0
        self.head = None
        self.tail = None 
    
    def push_front(self, data):
        new_node = Node(data) # 새 노드 만들기
        if not self.head: 
            self.head = self.tail = new_node
        else: 
            new_node.next = self.head 
            self.head.prev = new_node
            self.head = new_node
        self.node_num += 1

    def push_back(self, data):
        new_node = Node(data) # 새 노드 만들기
        if not self.tail: 
            self.head = self.tail = new_node
        else: 
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.node_num += 1
    
    def pop_front(self):
        if not self.head: # 만약에 아무 노드도 없다면
            return -1
        data = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head.prev = None # 지금 헤드의 prev을 초기화 
            self.head = self.head.next # 다음 노드가 헤드가 됨
        self.node_num -= 1 
        return data 
    
    def pop_back(self):
            if not self.tail:
                return -1
            
            data = self.tail.data
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            self.node_num -= 1
            return data

N = int(input())
dl_list = DoublyLinkedList()
ans = []

for _ in range(N):
    line = input().split()
    cmd = line[0]

    if cmd == 'push_front':
        dl_list.push_front(int(line[1]))
    elif cmd == 'push_back':
        dl_list.push_back(int(line[1]))
    elif cmd == 'pop_front':
        ans.append(dl_list.pop_front())
    elif cmd == 'pop_back':
        ans.append(dl_list.pop_back())
    elif cmd == 'size':
        ans.append(dl_list.node_num)
    elif cmd == 'empty':
        ans.append(1 if dl_list.node_num == 0 else 0)
    elif cmd == 'front':
        ans.append(dl_list.head.data if dl_list.head else -1)
    elif cmd == 'back':
        ans.append(dl_list.tail.data if dl_list.tail else -1)

print(*ans, sep='\n', end='\n')