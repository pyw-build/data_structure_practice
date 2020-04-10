import my_graph
import my_stack_queue

def BFS(graph, queue, vertices_list, start_point, start_level):
    for item in graph.adjacency_list[start_point]:
        if not vertices_list[item][0]:
            vertices_list[item] = [start_point, start_level+1]
            queue.add(item)
            print(f'item: {item}, start_point: {start_point}, level: {start_level+1}')

def DFS(graph, vertices_list, start_point, start_level):
    for item in graph.adjacency_list[start_point]:
        if not vertices_list[item][0]:
            vertices_list[item] = [start_point, start_level+1]
            print(f'item: {item}, start_point: {start_point}, level: {start_level+1}')
            DFS(graph, vertices_list, item, start_level+1)            
    return

if __name__ == "__main__":

    #vertices_names = ['A','B','C','D','E','F','G','H']
    vertices_names = ['A','B','C','D','E','F','G','H','I']
    vertices_to_be_added = {}
    for item in vertices_names:
        vertices_to_be_added[item] = [None, 0]
    print(vertices_to_be_added)

    edges_to_be_added = []
    '''
    edges_to_be_added.append(my_graph.myEdge('A','B',1))
    edges_to_be_added.append(my_graph.myEdge('A','C',1))
    edges_to_be_added.append(my_graph.myEdge('B','D',1))
    edges_to_be_added.append(my_graph.myEdge('B','E',1))
    edges_to_be_added.append(my_graph.myEdge('E','F',1))
    edges_to_be_added.append(my_graph.myEdge('C','F',1))
    edges_to_be_added.append(my_graph.myEdge('C','G',1))
    edges_to_be_added.append(my_graph.myEdge('F','G',1))
    edges_to_be_added.append(my_graph.myEdge('E','H',1))
    '''
    edges_to_be_added.append(my_graph.myEdge('A','B',1))
    edges_to_be_added.append(my_graph.myEdge('A','C',1))
    edges_to_be_added.append(my_graph.myEdge('A','D',1))
    edges_to_be_added.append(my_graph.myEdge('B','E',1))
    edges_to_be_added.append(my_graph.myEdge('C','E',1))
    edges_to_be_added.append(my_graph.myEdge('C','H',1))
    edges_to_be_added.append(my_graph.myEdge('D','H',1))
    edges_to_be_added.append(my_graph.myEdge('E','F',1))
    edges_to_be_added.append(my_graph.myEdge('C','F',1))
    edges_to_be_added.append(my_graph.myEdge('C','G',1))
    edges_to_be_added.append(my_graph.myEdge('H','G',1))
    edges_to_be_added.append(my_graph.myEdge('F','I',1))
    edges_to_be_added.append(my_graph.myEdge('G','I',1))
    print(edges_to_be_added)

    my_graph_test = my_graph.myGraph()
    for item in vertices_to_be_added:
        my_graph_test.adjacency_list[item] = []
    print(my_graph_test.adjacency_list)
    # treat each edge as in undirected graph:
    for item in edges_to_be_added:
        my_graph_test.adjacency_list[item.start].append(item.end)
        my_graph_test.adjacency_list[item.end].append(item.start)
    print(my_graph_test.adjacency_list)

    #BFS
    print("=== BFS ===")
    my_v_queue = my_stack_queue.myQueue(len(vertices_to_be_added))
    #start from 'A'
    my_v_queue.add('A')
    vertices_to_be_added['A']=['visited',0]
    start_point = 'A'
    start_level = 0
    while not my_v_queue.isEmpty():
        BFS(my_graph_test, my_v_queue, vertices_to_be_added, start_point, start_level)
        start_point = my_v_queue.delete()
        start_level = vertices_to_be_added[start_point][1]

    #DFS
    print("=== DFS ===")
    #reset
    for key in vertices_to_be_added:
        vertices_to_be_added[key] = [None, 0]

    vertices_to_be_added['A']=['visited',0]
    start_point = 'A'
    start_level = 0
    DFS(my_graph_test, vertices_to_be_added, start_point, start_level)
    
    