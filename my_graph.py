class myVertex:
    def __init__(self,data_input):
        self.data=data_input

class myEdge:
    def __init__(self,start,end,weight):
        self.start=start
        self.end=end
        self.weight=weight

class myGraph:
    def __init__(self):
        self.vertices = []
        self.edges = []


if __name__ == "__main__":
    
    #initialize graph
    myGraphTest = myGraph()
    vertice_file = open("Vertices.txt", "r")
    for item in vertice_file.read().splitlines():
        myVertexTest = myVertex(item)
        myGraphTest.vertices.append(myVertexTest)
        print(myVertexTest.data)

    edge_file = open("Edges.txt", "r")
    for item in edge_file.read().splitlines():
        first_comma = item.find(',')
        second_comma = first_comma+1+item[first_comma+1:].find(',')
        myEdgeTest = myEdge(item[1:first_comma],item[first_comma+2:second_comma],int(item[second_comma+2:-1]))
        myGraphTest.edges.append(myEdgeTest)
        print("start: "+str(myEdgeTest.start)+", end:"+str(myEdgeTest.end)+", weight:"+str(myEdgeTest.weight))

    #get user input on the starting and end stations
    start_v = input("Please enter the starting station: ")
    end_v = input("Please enter the end station: ")

    


    

