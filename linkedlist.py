from typing import List, Any, Optional

class Node: 
    def __init__(self, data: Any) -> None: 
        self.data = data
        self.next = None

class LinkedList: 
    def __init__(self) -> None:
        self.head = None
        self.tail = None 
        self.size = 0 

    def insert_at_beginning(self, data: Any) -> None: 
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else: 
            node.next = self.head
            self.head = node 
        self.size += 1

    def insert_at_end(self, data: Any) -> None: 
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node 
        else: 
            self.tail.next = node
            self.tail = node 
        self.size += 1

    def delete_from_beginning(self) -> Optional[Any]:
        if not self.head:
            print("List is empty.")
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return data

    def delete_from_end(self) -> Optional[Any]:
        if not self.head:
            print("List is empty.")
            return None
        if self.head == self.tail:
            data = self.head.data
            self.head = self.tail = None
            self.size -= 1
            return data
        current = self.head
        while current.next != self.tail:
            current = current.next
        data = self.tail.data
        self.tail = current
        self.tail.next = None
        self.size -= 1
        return data

    def find(self, data: Any) -> bool:
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def get_size(self) -> int:
        return self.size

    def to_list(self) -> List[Any]:
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def print_list(self) -> None: 
        if not self.head: 
            print("Empty")
        else: 
            temp = self.head 
            while temp: 
                print(temp.data, end=" -> ")
                temp = temp.next 
            print("None")


if __name__ == "__main__":
    llist = LinkedList() 
    llist.insert_at_beginning(1) 
    llist.insert_at_beginning(2) 
    llist.insert_at_end(4)

    print("List after insertions:")
    llist.print_list()

    print("\nDeleted from beginning: ", llist.delete_from_beginning())
    print("List after deletion from beginning:")
    llist.print_list()

    print("\nDeleted from end: ", llist.delete_from_end())
    print("List after deletion from end:")
    llist.print_list()

    print("\nFinding element 1:", llist.find(1))
    print("Finding element 3:", llist.find(3))

    print("\nCurrent size of the list:", llist.get_size())

    print("\nList to Python list:", llist.to_list())
      
      
      
    