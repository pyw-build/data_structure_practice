import random

class myHeapNode:
    def __init__(self, key_input, data_input):
        self.key = key_input
        self.data = data_input
    
    def __repr__(self):
        return "Node key: "+str(self.key)+", node data: "+str(self.data)

class myMinHeap:
    def __init__(self):
        self.root = None
        self.heapList = [None] #Set [1] as the root node in order to apply convenient heap index manipulation

    def __repr__(self):
        key_list = []
        for item in self.heapList[1:]:
            key_list.append(item.key)
        return "Heap keys: "+str(key_list)

    #Insert at the end of array then bubble-up
    def insert(self, new_node):
        self.heapList.append(new_node)
        child_idx = len(self.heapList)-1 #The newly inserted element
        if child_idx==1: #root
            self.root = self.heapList[child_idx]
        else: #other node
            self.bubble_up(child_idx)

    def bubble_up(self, child_idx):
        parent_idx = self.getParentIdx(child_idx)
        while (parent_idx>=1) and (self.heapList[child_idx].key<self.heapList[parent_idx].key): #(parent_idx>=1) should be checked first
            #print("child idx: "+str(child_idx)+", parent idx: "+str(parent_idx))
            self.swapNodeContent(child_idx,parent_idx)
            child_idx = parent_idx
            parent_idx = self.getParentIdx(child_idx)

    def decreaseKey(self, child_idx, new_key):
        self.heapList[child_idx].key = new_key
        self.bubble_up(child_idx)

    #Delete the root, move the last element to the root, then bubble-down
    def extract(self):
        #move the last element to the root
        self.swapNodeContent(1,len(self.heapList)-1)
        node_to_return = self.heapList[-1]
        del self.heapList[-1]

        parent_idx = 1

        if len(self.heapList)==2: #extracting the root
            self.root = None           
        else: #bubble-down 
            left_child_idx = parent_idx*2
            right_child_idx = parent_idx*2+1
            while left_child_idx<len(self.heapList): #at least left child exist
                #print("left child idx: "+str(left_child_idx)+", parent idx: "+str(parent_idx))
                if right_child_idx>=len(self.heapList): #no right child
                    if self.heapList[parent_idx].key>self.heapList[left_child_idx].key:
                        #print("left child key: "+str(self.heapList[left_child_idx].key))
                        #print("parent key: "+str(self.heapList[parent_idx].key))
                        self.swapNodeContent(parent_idx,left_child_idx)
                        parent_idx = left_child_idx
                        left_child_idx = parent_idx*2
                        right_child_idx = parent_idx*2+1
                    else:
                        break #no swap means already reach heap status => break here
                else: #both left and right child exist
                    #swap with the larger child if parent is larger than that child
                    min_child = self.heapList[left_child_idx].key if self.heapList[left_child_idx].key<self.heapList[right_child_idx].key else self.heapList[right_child_idx].key
                    #print("left child key: "+str(self.heapList[left_child_idx].key))
                    #print("right child key: "+str(self.heapList[right_child_idx].key))
                    #print("parent key: "+str(self.heapList[parent_idx].key))
                    if (min_child == self.heapList[left_child_idx].key) and (self.heapList[parent_idx].key>self.heapList[left_child_idx].key): #swap parent with left child
                        self.swapNodeContent(parent_idx,left_child_idx)
                        parent_idx = left_child_idx
                        left_child_idx = parent_idx*2
                        right_child_idx = parent_idx*2+1
                    elif (min_child == self.heapList[right_child_idx].key) and (self.heapList[parent_idx].key>self.heapList[right_child_idx].key):
                        self.swapNodeContent(parent_idx,right_child_idx)
                        parent_idx = right_child_idx
                        left_child_idx = parent_idx*2
                        right_child_idx = parent_idx*2+1
                    else:
                        break #no swap means already reach heap status => break here
        return node_to_return
    
    def getParentIdx(self,child_idx):
        return (int(child_idx/2) if (child_idx%2==0) else int(child_idx/2)) #int() gets floor effectively. To be clear, judge even/odd here

    def swapNodeContent(self, idx_a, idx_b):
        tmp = self.heapList[idx_a]
        self.heapList[idx_a] = self.heapList[idx_b]
        self.heapList[idx_b] = tmp

    def isEmpty(self):
        return (len(self.heapList)==1)

if __name__ == "__main__":

    list_A=random.sample(range(100),10)

    myMinHeapTest = myMinHeap()
    for item in list_A:
        myHeapNodeTest = myHeapNode(item,"Test_"+str(item))
        myMinHeapTest.insert(myHeapNodeTest)
    print(myMinHeapTest)

    while not myMinHeapTest.isEmpty():
        extract_node = myMinHeapTest.extract()
        print(extract_node.key)