import my_heap

class myVertex:
    def __init__(self,data_input):
        self.data=data_input
        self.prev_v="" #previous vertex in the shortest path

    def __repr__(self):
        return myVertexTest.data

class myEdge:
    def __init__(self,start,end,weight):
        self.start=start
        self.end=end
        self.weight=weight

    def __repr__(self):
        return ("start: "+str(self.start)+", end:"+str(self.end)+", weight:"+str(self.weight))

class myGraph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def binarySearchEdge(self,key,list_in,start,end):
        if end>=start:
            middle_idx = int((start+end)/2)
            if key==list_in[middle_idx].start:
                return middle_idx
            elif key>list_in[middle_idx].start:
                return self.binarySearchEdge(key,list_in,middle_idx+1,end)
            else:
                return self.binarySearchEdge(key,list_in,start,middle_idx-1)

    def searchEdge(self,start_v):
            found_list = []
            found_idx = self.binarySearchEdge(start_v,self.edges,0,len(self.edges)-1) #first found idx
            while found_idx:
                #print(len(self.edges))
                found_list.append(self.edges[found_idx])
                del self.edges[found_idx]
                found_idx = self.binarySearchEdge(start_v,self.edges,0,len(self.edges)-1)
            return found_list

if __name__ == "__main__":
    
    #initialize graph
    myGraphTest = myGraph()
    vertice_file = open("Vertices.txt", "r")
    for item in vertice_file.read().splitlines():
        myVertexTest = myVertex(item)
        myGraphTest.vertices.append(myVertexTest)
        #print(myVertexTest)

    edge_file = open("Edges.txt", "r")
    for item in edge_file.read().splitlines():
        first_comma = item.find(',')
        second_comma = first_comma+1+item[first_comma+1:].find(',')
        myEdgeTest = myEdge(item[1:first_comma],item[first_comma+2:second_comma],int(item[second_comma+2:-1]))
        myGraphTest.edges.append(myEdgeTest)
        #print(myEdgeTest)

    #get user input on the starting and end stations
    # start_v = input("Please enter the starting station: ")
    # end_v = input("Please enter the end station: ")
    start_v = "Greenwich"
    end_v = "Hendon_Central"

    #Dijkstra’s algorithm

    #initialize heap: key of each heap node is its min distance from starting point)
    myVerticeHeap = my_heap.myMinHeap()
    for item in myGraphTest.vertices:
        if item.data==start_v:
            myHeapNodeTest = my_heap.myHeapNode(0,item)
            myVerticeHeap.insert(myHeapNodeTest)
        else:
            myHeapNodeTest = my_heap.myHeapNode(float("inf"),item)
            myVerticeHeap.insert(myHeapNodeTest)
        #print(myHeapNodeTest.data.data)

    visited_vertices = []

    while not myVerticeHeap.isEmpty():
        #extract vertex with min recorded distance from the heap, and added into visited list
        visited_vertices.append(myVerticeHeap.extract())  
        #print("Start from: "+(visited_vertices[-1].data.data))

        #update all edges from starting point
        found_list = myGraphTest.searchEdge(visited_vertices[-1].data.data)
        #print(found_list)

        for item in found_list:
            found = False
            #search for the end nodes
            for idx in range(1,len(myVerticeHeap.heapList)):
                if myVerticeHeap.heapList[idx].data.data == item.end:
                    found = True
                    break
            if found:
                #print("found idx: "+str(idx)+", data: "+(myVerticeHeap.heapList[idx].data.data))
                #print("heap len: "+str(len(myVerticeHeap.heapList)))
                new_distance = visited_vertices[-1].key+item.weight
                if new_distance<myVerticeHeap.heapList[idx].key:
                    myVerticeHeap.heapList[idx].data.prev_v = item.start
                    myVerticeHeap.decreaseKey(idx, new_distance)
        #print(myVerticeHeap)

    #output results
    current_v = end_v
    shortes_path = []
    while current_v!=start_v:
        #searching in 
        for idx in range(len(visited_vertices)):
            if visited_vertices[idx].data.data == end_v:
                total_cost = visited_vertices[idx].key
            if visited_vertices[idx].data.data == current_v:
                break
        shortes_path = [visited_vertices[idx].data.data]+shortes_path
        current_v = visited_vertices[idx].data.prev_v

    shortes_path = [start_v]+shortes_path

    #print shortest path
    print("Shortest path from "+start_v+" to "+end_v+": ")
    print(shortes_path)
    print("Cost: "+str(total_cost))



    

