import random
import my_sort

def mybinarysearch(key,list_in,start,end):
    if end>=start:
        middle_idx = int((start+end)/2)
        if key==list_in[middle_idx]:
            return middle_idx
        elif key>list_in[middle_idx]:
            return mybinarysearch(key,list_in,middle_idx+1,end)
        else:
            return mybinarysearch(key,list_in,start,middle_idx-1)

if __name__ == "__main__":
    list_A=random.sample(range(1000),100)
    key_to_search = 157
    print("original list: "+str(list_A))
    my_sort.my_quicksort(list_A,0,len(list_A))
    print("sorted list  : "+str(list_A))
    print("test result  : "+my_sort.test_sorted(list_A))

    found_idx = mybinarysearch(key_to_search,list_A,0,len(list_A)-1)
    print(found_idx)
    print(key_to_search)
    if found_idx:
        print(list_A[found_idx])