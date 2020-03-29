class myLinkedNode:
    def __init__(self, content_in):
        self.content = content_in
        self.next = None

class myLinkedList:
    def __init__(self):
        self.head = None
        self.listlength = 0

    def insert_at_end(self, content_in):
        newNode = myLinkedNode(content_in)
        if self.head==None:
            self.head=newNode
        else:
            positionToAppend = self.head
            while positionToAppend.next!=None:
                positionToAppend = positionToAppend.next
            positionToAppend.next = newNode
        self.listlength+=1

    def insert_at_middle(self, content_in,index):
        if index>self.listlength:
            print("Cannot insert at this middle index!")
        else:
            newNode = myLinkedNode(content_in)
            positionToAppend = self.head
            traverseCount = 0
            while traverseCount!=(index-1):
                positionToAppend = positionToAppend.next
                traverseCount+=1
            tmp = positionToAppend.next
            positionToAppend.next = newNode
            newNode.next = tmp
            self.listlength+=1

    def delete(self, content_in):
        pass
    def traverse(self):
        positionToPrint = self.head
        while positionToPrint!=None:
            print(positionToPrint.content)
            positionToPrint = positionToPrint.next

if __name__ == "__main__":
    myLinkedListTest = myLinkedList()
    myLinkedListTest.insert_at_end("AA")
    myLinkedListTest.insert_at_end("BB")
    myLinkedListTest.insert_at_end("CC")
    myLinkedListTest.insert_at_end("DD")
    myLinkedListTest.insert_at_end("EE")
    myLinkedListTest.insert_at_end("FF")
    myLinkedListTest.insert_at_middle("ZZ",2)
    myLinkedListTest.insert_at_middle("XX",4)
    myLinkedListTest.insert_at_middle("YY",6)
    myLinkedListTest.insert_at_middle("UU",100)
    myLinkedListTest.traverse()
    print(myLinkedListTest.listlength)