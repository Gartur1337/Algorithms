import random
from statistics import mean
from random import randint
import datetime

class People:
    def __init__(self, bd = None, first_name = None, last_name = None):
        self.bd = datetime.datetime(bd if bd else random.randint(1980, 2020), randint(1,12), randint(1,28))
        self.first_name = first_name if first_name else random.choice(['Artur', 'Vova', 'Maxim', 'Arion', 'Slava', 'Billy', 'Bob'])
        self.last_nam = last_name if last_name else random.choice(['Butilkin','Ivanov', 'Kharlamov', 'Morgenshtern', 'Mujik', 'Shlyapa'])

class Node(object):
    def __init__(self, item): 
        
        self.item = item
        self.next = None

    def increment(self):
        num = self.num
        self.num += 1
        return num

class queue:
    def __init__(self):
        self.head = None
        self.count = 0
    
    def is_empty(self):
        return self.head is None
    
    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            s = self.head
            while s.next:
                s = s.next
            s.next = node
        self.count += 1

    def len(self):
        return self.count

    def pop(self):
        out = self.head.item
        self.head = self.head.next
        self.count -= 1
        return out
        
    def sort_queue(self):
        if self.is_empty():
            return
        arr = []
        cur_node = self.head
        arr.append(cur_node.item)
        while cur_node.next:
            cur_node = cur_node.next
            arr.append(cur_node.item)
        arr.sort()
        while self.count:
            self.pop()
        for i in arr:
            self.append(i)
   
    def output_queue(self):
        if self.is_empty():
            arr = ''
        else:
            cur_node = self.head
            arr = []
            arr.append(cur_node.item)
            while cur_node.next:
                cur_node = cur_node.next
                arr.append(cur_node.item)
        print(arr)

def first_test():
    first_queue = queue()
    items = []

    for i in range(-1000, 1001, 1): first_queue.append(i)
        
    for i in range(first_queue.len()):
        items.append(first_queue.pop())

    print('max = {}, min = {}, average = {}, amount = {} '.format(max(items), min(items), mean(items), sum(items)))

def second_test():
    second_queue = queue()
    str_elements = []

    for i in range(65, 75): str_elements.append(chr(i))

    for i in str_elements:
        second_queue.append(i)
        second_queue.output_queue()
    print('Queue full of string elements')

    for i in range(second_queue.len()):
        second_queue.pop()
        second_queue.output_queue()
    
def third_test():
    third_queue = queue()
    res_queue_20 = queue()
    res_queue_30 = queue()
    counter = 0
    peoples = [People() for i in range(100)]
    today = datetime.datetime.now()
    for people in peoples:
        third_queue.append(people)
    while not third_queue.is_empty():
        human = third_queue.pop()
        diff = today - human.bd
        if diff.days // 365 < 20:
            res_queue_20.append(human)
        if diff.days // 365 > 30:
            res_queue_30.append(human)
        else:
            counter += 1
    print(counter)

def fourth_test():
    fourth_queue = queue()
    arr = []
    fourth_queue.append(random.randint(300, 2500) for i in range(1000))
    fourth_queue.sort_queue()

    for i in range(fourth_queue.len()):
        arr.append(fourth_queue.pop())

    sorted_arr = sorted(arr)
    if sorted_arr == arr:
        return print(True)

def fifth_test():
    fifth_queue = queue()
    arr = []
    for i in range(11): fifth_queue.append(i)
    fifth_queue.output_queue()
    while not fifth_queue.is_empty(): arr.append(fifth_queue.pop())
    
    for i in range(len(arr) -1, -1, -1):
        fifth_queue.append(arr[i])
    fifth_queue.output_queue()

def main():
    print("-" * 10, "First test", "-" * 10, '\n')
    first_test()
    print("-" * 100 + '\n')
    print("-" * 10, "Second test", "-" * 10, '\n')
    second_test()
    print("-" * 100 + '\n')
    print("-" * 10, "Third test", "-" * 10, '\n')
    third_test()
    print("-" * 100 + '\n')
    print("-" * 10, "Fourth test", "-" * 10, '\n')
    fourth_test()
    print("-" * 100 + '\n')
    print("-" * 10, "Fifth test", "-" * 10, '\n')
    fifth_test()

if __name__ == '__main__':
    main()