import random

def my_quicksort(list_in):
    if len(list_in)<1:
        return list_in
    else:
        pivot=list_in[len(list_in)-1]
        list_smaller=[]
        list_larger=[]
        for item in list_in[0:(len(list_in)-1)]:
            if item<pivot:
                list_smaller+=[item]
            else:
                list_larger+=[item]
        return my_quicksort(list_smaller)+[pivot]+my_quicksort(list_larger)



if __name__=='__main__':
    list_A=random.sample(range(100),20)
    print("original list: "+str(list_A))
    print("sorted list  : "+str(my_quicksort(list_A)))
