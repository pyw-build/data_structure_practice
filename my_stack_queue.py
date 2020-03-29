class myNode:
    def __init__(self, content_in):
        self.content = content_in

class myStack:
    def __init__(self, size):
         self.maxSize = size
         self.stackList = []
    def push(self,new_node):
        if len(self.stackList)==self.maxSize:
            print("Stack full! Cannot push!")
        else:
            self.stackList.append(new_node)
    def pop(self):
        if len(self.stackList) == 0:
            print("Stack empty! Cannot pop!")
            return None
        else:
            popItem = self.stackList[-1]
            del self.stackList[-1]
            return popItem
    def isFull(self):
        return len(self.stackList) == self.maxSize
    def isEmpty(self):
        return len(self.stackList) == 0

class myQueue:
    def __init__(self, size):
        self.maxSize = size
        self.queueList = []  #front: , rear: 
    def add(self,new_node):
        if len(self.queueList)==self.maxSize:
            print("Queue full! Cannot add!")
        else:
            self.queueList.append(new_node)
    def delete(self):
        if len(self.queueList)==0:
            print("Queue empty! Cannot delete!")
        else:
            delItem = self.queueList[0]
            del self.queueList[0]
            return delItem
    def front(self):
        if len(self.queueList)!=0:
            return self.queueList[0]
    def rear(self):
        if len(self.queueList)!=0:
            return self.queueList[-1]
    def isFull(self):
        return len(self.queueList) == self.maxSize
    def isEmpty(self):
        return len(self.queueList) == 0

if __name__ == "__main__":
    #Stack test
    myStacktest = myStack(5)
    #Push test
    for i in range(6):
        myStacktest.push(myNode(i*101))
        #print("Push: "+str(i*101))
    #Pop test
    for i in range(6):
        popItem = myStacktest.pop()
        if popItem!=None:
            print("Pop: "+str(popItem.content))

    #Queue test
    myQueuetest = myQueue(5)
    #Add test
    for i in range(6):
        myQueuetest.add(myNode(i*11))
    #Delete test
    for i in range(6):
        delItem = myQueuetest.delete()
        if delItem!=None:
            print("Delete: "+str(delItem.content))