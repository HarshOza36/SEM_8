# Creating Node structure for circular linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Creating the linked list
class CreateCircularLinkList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head

    def add_node(self, data):
        newNode = Node(data)
        if self.head.data is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.tail.next = self.head

    def display(self):
        current = self.head
        if self.head is None:
            print("No process in Ring")
            return
        else:
            print("\nProcess are >>>> ")
            print(current.data, end=" >> ")
            while(current.next != self.head):
                current = current.next
                print(current.data, end=" >> ")

    def deleteTail(self):
        if(self.head == None):
            return
        else:
            if(self.head != self.tail):
                current = self.head
                while(current.next != self.tail):
                    current = current.next
                print(f"\nOh Node {self.tail.data} has crashed !!")
                self.tail = current
                self.tail.next = self.head
            else:
                self.head = self.tail = None

    def countNodes(self, head):
        temp = head
        result = 0
        if (head != None):
            while True:
                temp = temp.next
                result = result + 1
                if (temp == head):
                    break
        return result

    def findNode(self, current, node):
        coordinator = node
        while(current.next.data != coordinator):
            current = current.next
        current = current.next
        return current

    # Ring Algorithm
    def send(self):
        self.deleteTail()
        self.display()
        coordinator = int(
            input("\nEnter the process that notices the crash >>>> "))
        token_list = []
        current = self.head
        count = self.countNodes(current)
        current = self.findNode(current, coordinator)
        selected_coordinator = current
        for i in range(count):
            token_list.append(current.data)
            prev = current.data
            current = current.next
            print(
                f"Process-{prev} sends to Process-{current.data} with List : {token_list}")
        new_coordinator = max(token_list)
        print(
            f"\nCoordinator is {new_coordinator}\nInformation will be sent to all processes >>>> \n")
        current = selected_coordinator
        for i in range(count-1):
            prev = current.data
            current = current.next
            print(
                f"Process-{prev} sends to Process-{current.data} saying Coordinator is {new_coordinator}")


# Initializing the Ring
ring = CreateCircularLinkList()

proc = int(input("Please enter the number of processes >>>> "))
# Adding process ids
for i in range(0, proc):
    ring.add_node(i+1)
ring.display()

# Apply Ring Algorithm
ring.send()
