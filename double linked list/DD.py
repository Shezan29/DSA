class Node:
    def __init__(self, value=None):
        self.data = value
        self.next = None
        self.prev = None


class DoublyLL:
    def __init__(self, head=None):
        self.head = head

    def insertEnd(self, value):
        temp = Node(value)

        if self.head == None:
            self.head = temp
        else:
            t = self.head

            while t.next != None:
                t = t.next

            t.next = temp
            temp.prev = t

    def insertBeg(self, value):
        temp = Node(value)

        if self.head == None:
            self.head = temp
        else:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp

    def insertMid(self, value, after):
        temp = Node(value)

        t = self.head
        while t != None:
            if t.data == after:
                break
            else:
                t = t.next

        if t.data == after:
            if t.next == None:
                temp.prev = t
                t.next = temp
            else:
                temp.next = t.next
                temp.prev = t
                t.next.prev = temp
                t.next = temp

    def deleteLL(self, value):
        t = self.head

        while t != None:
            if t.data == value:
                if t.prev == None:
                    self.head = t.next
                    if t.next != None:
                        t.next.prev = None

                elif t.next == None:
                    t.prev.next = None

                else:
                    t.prev.next = t.next
                    t.next.prev = t.prev
                break

            t = t.next

    def printDDL(self):
        t = self.head
        while t != None:
            print(t.data, end=" ")
            t = t.next


obj = DoublyLL()
obj.insertEnd(10)
obj.insertEnd(20)
obj.insertEnd(30)
obj.insertEnd(40)
obj.insertBeg(50)
obj.insertMid(333, 40)
obj.insertMid(555, 20)
obj.deleteLL(333)
obj.printDDL()
