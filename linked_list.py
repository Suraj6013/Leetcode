class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Menu
def menu():
    ll = LinkedList()
    while True:
        print("\n1. Insert")
        print("2. Print")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = int(input("Enter the data to insert: "))
            ll.insert(data)
        elif choice == 2:
            ll.print_list()
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")


menu()