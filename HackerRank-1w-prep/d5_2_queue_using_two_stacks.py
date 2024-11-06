class Node:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

    def __str__(self):
        return f"""{self.data}"""


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        str_repr = ''
        curr_node = self.head
        while curr_node is not None:
            str_repr += f""" {curr_node} """
            curr_node = curr_node.next
        return str_repr

    def is_empty(self):
        return self.size == 0

    def peek(self):
        if self.head is not None:
            return self.head.data
        else:
            return None

    def push(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def pop(self):
        if self.size == 0:
            x = None
        else:
            x = self.head.data
            self.head = self.head.next
            self.size -= 1
        return x


class Queue:
    def __init__(self):
        self.stack1 = Stack()  # FIFO: when stack1 is not empty, elements are stored here with the top being the first element in
        self.stack2 = Stack()  # LIFO: when stack2 is not empty, elements are stored here with the top being the last element in

    def __str__(self):
        return 'stack1: ' + str(self.stack1) + ', stack2:' + str(self.stack2)

    def dequeue(self):
        if self.stack1.is_empty():
            while not self.stack2.is_empty():
                self.stack1.push(self.stack2.pop())
        return self.stack1.pop()

    def enqueue(self, data):
        self.stack2.push(data)

    def print(self):
        if self.stack1.is_empty():
            while not self.stack2.is_empty():
                self.stack1.push(self.stack2.pop())
        print(self.stack1.peek())


if __name__ == '__main__':
    q = Queue()
    print('--- init queue:')
    print(q)

    q.enqueue(42)
    print('--- enqueue(42):')
    print(q)

    q.dequeue()
    print('--- dequeue():')
    print(q)

    q.enqueue(14)
    print('--- enqueue(14):')
    print(q)
    q.print()

    q.enqueue(28)
    print('--- enqueue(28):')
    print(q)
    q.print()

    q.enqueue(60)
    print('--- enqueue(60):')
    print(q)

    q.enqueue(78)
    print('--- enqueue(78):')
    print(q)

    q.dequeue()
    print('--- dequeue():')
    print(q)

    q.dequeue()
    print('--- dequeue():')
    print(q)

    if False: # main() code for HackerRank
        q = Queue()

        tests = int(input())

        for i in range(tests):
            s = input().split(' ')
            if int(s[0]) == 1:
                q.enqueue(int(s[1]))
            elif int(s[0]) == 2:
                q.dequeue()
            elif int(s[0]) == 3:
                q.print()

    if False:
        s = Stack()
        s.push(18)
        s.push(19)
        print(s)
        print(s.pop())
        print(s)