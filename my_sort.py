import random
import my_heap

def my_mergesort(list_in):
    if len(list_in)<=1:
        return list_in
    else: 
        half_len =int(len(list_in)/2)
        #print("list in: "+str(list_in))
        #sort the first half
        first_half = my_mergesort(list_in[0:half_len])
        #sort the second half
        second_half = my_mergesort(list_in[half_len:len(list_in)])
        #merge two sorted lists
        return merge(first_half, second_half)

def merge(list_a,list_b):
    merged_list = []
    list_a_cursor=0
    list_b_cursor=0
    #print("list a: "+str(list_a))
    #print("list b: "+str(list_b))
    while( list_a_cursor!=len(list_a) and list_b_cursor!=len(list_b) ):
        if list_a[list_a_cursor]<list_b[list_b_cursor]:
            merged_list.append(list_a[list_a_cursor])
            list_a_cursor+=1
        else:
            merged_list.append(list_b[list_b_cursor])
            list_b_cursor+=1
    if list_b_cursor!=len(list_b): #no item left in list_a, but something is left in list_b
        merged_list+=list_b[list_b_cursor:len(list_b)]
    elif list_a_cursor!=len(list_a): #no item left in list_b, but something is left in list_a
        merged_list+=list_a[list_a_cursor:len(list_a)]
    return merged_list

def my_quicksort(list_in,lo,hi):
    if hi>lo:
        index_p = partition(list_in, lo, hi)
        #sort the larger array
        my_quicksort(list_in,(index_p+1), hi)
        #sort the smaller array
        my_quicksort(list_in, lo, index_p)

def partition(list_in, lo, hi):
    pivot = list_in[lo] #the pivot is at list_in[0]
    smaller_head = lo+1 #head of smaller array 
    larger_head = lo+1 #head of larger array
    for larger_head in range(lo+1,hi):
        if list_in[larger_head]<pivot:
            swap(list_in, smaller_head, larger_head)
            smaller_head+=1
        #if larger than or equal to pivot, do not swap
    #swap the pivot with smaller_head
    swap(list_in, lo,smaller_head-1)
    #return the index of pivot
    return (smaller_head-1)

def swap(list_in,index_a,index_b):
    tmp=list_in[index_a]
    list_in[index_a]=list_in[index_b]
    list_in[index_b]=tmp

def test_sorted(list_in):
    for i in range(len(list_in)-1):
        if list_in[i]>list_in[i+1]:
            return "Sort Fail"
    return "Sort Pass"

def my_heapsort(list_in):
    myMinHeapTest = my_heap.myMinHeap()
    for item in list_in:
        myHeapNodeTest = my_heap.myHeapNode(item,"Test_"+str(item))
        myMinHeapTest.insert(myHeapNodeTest)

    sorted_list = []
    while not myMinHeapTest.isEmpty():
        extract_node = myMinHeapTest.extract()
        sorted_list.append(extract_node.key)
    return sorted_list

if __name__=='__main__':
    list_A=random.sample(range(1000),100)
    print("original list: "+str(list_A))
    my_quicksort(list_A,0,len(list_A))
    print("sorted list  : "+str(list_A))
    print("test result  : "+test_sorted(list_A))

    list_B=random.sample(range(1000),100)
    print("original list: "+str(list_B))
    sorted_list_B = my_mergesort(list_B)
    print("sorted list  : "+str(sorted_list_B))
    print("test result  : "+test_sorted(sorted_list_B))

    list_C=random.sample(range(1000),100)
    print("original list: "+str(list_C))
    sorted_list_C = my_heapsort(list_C)
    print("sorted list  : "+str(sorted_list_C))
    print("test result  : "+test_sorted(sorted_list_C))