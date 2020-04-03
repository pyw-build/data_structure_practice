class myTreeNode:
    def __init__(self, key_input, data_input):
        self.data = data_input
        self.key = key_input
        self.LeftChild = None
        self.RightChild = None

    def print(self):
        print(self.key)

class IndexEntry:
    def __init__(self, key_input, page):
        self.page_start = page
        self.page_end = page
        self.key = key_input
        self.LeftChild = None
        self.RightChild = None

    def print(self):
        print(str(self.key)+" "+str(self.page_start)+"-"+str(self.page_end))

class myBST:
    def __init__(self, root_node):
        self.root = root_node

    def insert(self, new_node):
        if self.root==None:
            self.root = new_node
        else:
            self.insert_check_node(self.root,new_node)

    def insert_check_node(self,node_to_compare,new_node): #assume no duplicate
        if new_node.key>node_to_compare.key:
            if node_to_compare.RightChild == None:
                node_to_compare.RightChild = new_node
            else:
                self.insert_check_node(node_to_compare.RightChild,new_node)
        elif new_node.key<node_to_compare.key:
            if node_to_compare.LeftChild == None:
                node_to_compare.LeftChild = new_node
            else:
                self.insert_check_node(node_to_compare.LeftChild,new_node)     

    def search(self,key_to_search):
        return self.search_check_node(self.root,None,0,key_to_search)


    def search_check_node(self,node_to_compare,parent,is_right,key_to_search): #is_right==True: target node is the RightChild of parent node
        if key_to_search == node_to_compare.key:
            print("Search succeeded. Key "+str(node_to_compare.key))
            return (node_to_compare,parent,is_right)
        elif key_to_search>node_to_compare.key:
            if node_to_compare.RightChild == None:
                print("Search failed. Key "+str(key_to_search)+" doesn't exist in the tree")
                return None
            else:
                return self.search_check_node(node_to_compare.RightChild,node_to_compare,1,key_to_search)
        elif key_to_search<node_to_compare.key:
            if node_to_compare.LeftChild == None:
                print("Search failed. Key "+str(key_to_search)+" doesn't exist in the tree")
                return None
            else:
                return self.search_check_node(node_to_compare.LeftChild,node_to_compare,0,key_to_search)    

    def delete(self,key_to_delete):
        (target_node,target_parent,is_right) = self.search(key_to_delete) #ignore the case that key_to_delete is not found
        
        #Case 1: deleting a leaf node
        if (target_node.LeftChild==None) and (target_node.RightChild==None) and (target_parent!=None): #ignore the case of deleting the root
            #delete this leaf node
            if is_right:
                target_parent.RightChild = None
            else:
                target_parent.LeftChild = None
        #Case 2: deleting a node that has one child
        elif (target_node.LeftChild==None):
            #move the sub-tree up
            if is_right:
                target_parent.RightChild = target_node.RightChild
            else:
                target_parent.LeftChild = target_node.RightChild
        elif (target_node.RightChild==None):
            #move the sub-tree up
            if is_right:
                target_parent.RightChild = target_node.LeftChild
            else:
                target_parent.LeftChild = target_node.LeftChild
        #Case 3: deleting a node that has two children
        else:
            #search the next largest in the right subtree, and replace the current node
            (next_largest_node,next_largest_parent,is_right) = self.find_min(target_node.RightChild,target_node,True)
            print("Replace "+str(target_node.key)+" with "+str(next_largest_node.key)+". is_right: "+str(is_right))
            target_node.key = next_largest_node.key #replace directly
            if is_right:
                next_largest_parent.RightChild = None #effectively delete the next largest node
            else:
                next_largest_parent.LeftChild = None #effectively delete the next largest node

    def find_min(self, starting_node, starting_parent, is_right):
        if starting_node.LeftChild == None:
            return (starting_node,starting_parent,is_right)
        else:
            return self.find_min(starting_node.LeftChild,starting_node, False)

    def inorder_traverse(self,node):
        if node.LeftChild:
            self.inorder_traverse(node.LeftChild)
        if node:
            node.print()
        if node.RightChild:
            self.inorder_traverse(node.RightChild)

    def postorder_traverse(self,node):
        if node.LeftChild:
            self.postorder_traverse(node.LeftChild)
        if node.RightChild:
            self.postorder_traverse(node.RightChild)
        if node:
            node.print()

    def preorder_traverse(self,node):
        if node:
            node.print()
        if node.LeftChild:
            self.preorder_traverse(node.LeftChild)
        if node.RightChild:
            self.preorder_traverse(node.RightChild)


if __name__ == "__main__":
    myBSTtest = myBST(None)
    value_to_insert=[30,5,40,2,7,35,80,1,6,32,75]

    for item in value_to_insert:
        myTreeNodeTest = myTreeNode(item, "Test_"+str(item))
        myBSTtest.insert(myTreeNodeTest)

    myBSTtest.inorder_traverse(myBSTtest.root)
    myBSTtest.postorder_traverse(myBSTtest.root)
    myBSTtest.preorder_traverse(myBSTtest.root)

    (mySearchNodeTest,ParentNode,is_right) = myBSTtest.search(30)
    print(mySearchNodeTest.data)

    #Search Test
    (target_node,target_parent, is_right) = myBSTtest.find_min(mySearchNodeTest,None,False)
    print(target_node.data)
    
    #Delete Test
    myBSTtest.delete(40)
    myBSTtest.inorder_traverse(myBSTtest.root)

    #String Test
    myStrBSTtest = myBST(None)
    value_to_insert = [("Series|(",2),("Series!geometric|(",4),("Euler’s constant",4),("Series!geometric|)",4),\
        ("Series!arithmetic|(",4),("Series!arithmetic|)",5),("Series!harmonic|(",5),\
        ("Series!harmonic|)",5),("Series|)",5)]

    for item in value_to_insert:
        string = item[0]
        page_num = item[1]
        if string[-2:]=="|(":
            myIndexEntry = IndexEntry(string[0:len(string)-2],page_num)
            myStrBSTtest.insert(myIndexEntry)
        elif string[-2:]=="|)":
            #Find corresponding item and update its end_page
            (myIndexEntry,ParentNode,is_right) = myStrBSTtest.search(string[0:len(string)-2])
            if page_num>= myIndexEntry.page_end:
                myIndexEntry.page_end = page_num
        else:
            myIndexEntry = IndexEntry(string,page_num)
            myStrBSTtest.insert(myIndexEntry)

    myBSTtest.inorder_traverse(myStrBSTtest.root)