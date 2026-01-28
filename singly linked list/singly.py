class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SinglyLL:
    def __init__(self, head=None):
        self.head = head

    def insertEnd(self, value):
        temp = Node(value)

        if self.head == None:
            self.head = temp
        else:
            t1 = self.head
            while t1.next != None:
                t1 = t1.next
            t1.next = temp

    def insertBeg(self, value):
        temp = Node(value)

        temp.next = self.head
        self.head = temp

    def insertMid(self, value, after):
        temp = Node(value)

        trv = self.head
        while trv != None:
            if trv.data == after:
                temp.next = trv.next
                trv.next = temp
                break

            trv = trv.next

    def deleteLL(self, value):
        trv = self.head
        prev = None

        if trv.data == value:
            self.head = trv.next
            return

        while trv != None:
            if trv.data == value:
                prev.next = trv.next
                return
            prev = trv
            trv = trv.next

    def printLL(self):
        t1 = self.head

        while t1 != None:
            print(t1.data)
            t1 = t1.next


link1 = SinglyLL()
link1.insertEnd(10)
link1.insertEnd(20)
link1.insertEnd(40)
link1.insertEnd(30)
link1.insertBeg(-89)
link1.insertMid(222, 40)

link1.deleteLL(30)

link1.printLL()
