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
    list_bolt=random.sample(range(2000),1000)
    list_nut=list_bolt*1
    random.shuffle(list_nut)
    print("Original list bolt: "+str(list_bolt))
    print("Original list nut : "+str(list_nut))
    compare_nut_and_bolt(list_nut,list_bolt,0,len(list_bolt)-1)
    print("Arranged list bolt: "+str(list_bolt))
    print("Arranged list nut : "+str(list_nut))
    print("Check result: "+str(list_nut==list_bolt))
