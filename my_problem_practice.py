##################################################
# Nuts & Bolts Problem
# Match nuts and bolts
#
# Assumptions:
# 1. All sizes are different
# 
# Steps:
# 1. Find a pivot nut i. Compare all bolts with nut i and find bolt i. Compare all nut with bolt i. O(n)+O(n)
# 2. Divide bolts and nuts into two groups: size>=size(i)), size<=size(i)
# 3. Repeat for subarraies. O(logn) layers
##################################################
import random
import my_stack_queue

def partition(array_in, start_idx, end_idx, pivot):
    #print("============ array_in : "+str(array_in[start_idx:end_idx+1]))
    smaller_head = start_idx+1 #reserve [start_idx] for pivot
    i = start_idx+1
    while i<(end_idx+1):
        if array_in[i]<pivot:
            #print("swap: "+str(array_nut[i]))
            swap(array_in,smaller_head,i)
            smaller_head+=1
        elif array_in[i]==pivot:
            swap(array_in,start_idx,i) #move pivot to head
            #to keeo the same i(as this element needs to be checked after swapped with pivot)
            i-=1
        i+=1
    swap(array_in,start_idx,smaller_head-1) #put pivot in the correst place
    pivot_idx=smaller_head-1
    #print("smaller n: "+str(array_in[start_idx:pivot_idx]))
    #print("pivot_idx: "+str(pivot_idx))
    #print("pivot: "+str(array_in[pivot_idx]))
    #print("larger n: "+str(array_in[pivot_idx+1:end_idx+1]))
    return pivot_idx

def swap(array_in, index_a, index_b):
    tmp = array_in[index_a]
    array_in[index_a] = array_in[index_b]
    array_in[index_b] = tmp

def compare_nut_and_bolt(array_nut, array_bolt, start_idx, end_idx):
    if start_idx >= end_idx:
        pass
    else:
        pivot_idx = partition(array_nut, start_idx, end_idx, array_bolt[start_idx])
        partition(array_bolt, start_idx, end_idx, array_nut[pivot_idx])
        compare_nut_and_bolt(array_nut, array_bolt, start_idx, pivot_idx-1) #handle the smaller array
        compare_nut_and_bolt(array_nut, array_bolt, pivot_idx+1, end_idx) #handle the smaller array

if __name__=="__main__":
    # bolts and nuts problem
    list_bolt=random.sample(range(2000),1000)
    list_nut=list_bolt*1
    random.shuffle(list_nut)
    print("Original list bolt: "+str(list_bolt))
    print("Original list nut : "+str(list_nut))
    compare_nut_and_bolt(list_nut,list_bolt,0,len(list_bolt)-1)
    print("Arranged list bolt: "+str(list_bolt))
    print("Arranged list nut : "+str(list_nut))
    print("Check result: "+str(list_nut==list_bolt))

    # mouse in the maze problem
    # ignore user-input maze
    '''
    maze_width = int(input("Please input maze width m: "))
    maze_height = int(input("Please input maze height n: "))
    maze_content = []
    for i in range(maze_width):
        maze_content.append([])
        for j in range(maze_height):
            maze_content[i].append(int(input("Please input maze content (%d,%d): "%(i,j))))
    '''
    maze_width = 4
    maze_height = 4
    maze_content = [[12,5,1,7],[11,9,0,7],[12,2,12,7],[13,4,5,2]]

    #ignore maze validity check 
    print(maze_content)
    start_point=(0,0)
    end_point=(maze_width-1,maze_height-1)
    print("start:(%d,%d), end:(%d,%d)"%(start_point[0],start_point[1],end_point[0],end_point[1]))

    current_x=start_point[0]
    current_y=start_point[1]
    prev_x=maze_width  #initialize as a large num
    prev_y=maze_height #initialize as a large num
    offsets = [[-1,0],[0,1],[1,0],[0,-1]] #toward W,S,E,N
    myMazeStack = my_stack_queue.myStack(maze_width*maze_height)
    myMazeStack.push((current_x,current_y,0,0,0))
    direction_idx_start = 0

    while (  ((current_x==end_point[0])&(current_y==end_point[1])==False)  ) & (~myMazeStack.isEmpty()) & (~myMazeStack.isFull()):
        #check W,S,E,N
        #start from the previous index searched, as this turn be back from invalid path 
        for direction_idx in range(direction_idx_start,4): 
            new_x=current_x+offsets[direction_idx][0]
            new_y=current_y+offsets[direction_idx][1]
            #print("New (%d,%d)"%(new_x,new_y))
            #print(direction_idx)
            #print(maze_content[current_x][current_y]&(0b1<<direction_idx))
            found = False
            if ((maze_content[current_x][current_y]&(0b1<<direction_idx))==0) & \
            (new_x in range(maze_width)) & \
            (new_y in range(maze_height)) & \
            ( ((new_x==prev_x)&(new_y==prev_y)==False) ): #can go toward this direction
                myMazeStack.push((new_x,new_y,current_x,current_y,direction_idx))  #also record the direction index in case of future search from this point
                prev_x = current_x
                prev_y = current_y
                current_x = new_x
                current_y = new_y
                #print("Go to (%d,%d), value: %d"%(current_x,current_y,maze_content[current_x][current_y]))
                found = True
                direction_idx_start = 0
                break
        #after searching the four directions and found that no direction to go: pop out stack element and search again
        if found == False:
            (prev_x, prev_y, current_x, current_y, invalid_direction_idx) = myMazeStack.pop()
            #print("Back to (%d,%d), prev (%d,%d)"%(current_x,current_y,prev_x,prev_y) )
            direction_idx_start = invalid_direction_idx+1
        
    #print out solution
    while myMazeStack.isEmpty()!=True:
        print(myMazeStack.pop())
    
    #ignore graphic output
