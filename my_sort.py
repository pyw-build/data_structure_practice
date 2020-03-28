import random

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

if __name__=='__main__':
    list_A=random.sample(range(1000),100)
    print("original list: "+str(list_A))
    my_quicksort(list_A,0,len(list_A))
    print("sorted list  : "+str(list_A))
    print("test result  : "+test_sorted(list_A))
