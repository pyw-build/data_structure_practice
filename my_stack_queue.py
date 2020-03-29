class myStackNode:
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

if __name__ == "__main__":
    myStacktest = myStack(5)
    #Push test
    for i in range(6):
        myStacktest.push(myStackNode(i*101))
        #print("Push: "+str(i*101))
    #Pop test
    for i in range(6):
        popItem = myStacktest.pop()
        if popItem!=None:
            print("Pop: "+str(popItem.content))