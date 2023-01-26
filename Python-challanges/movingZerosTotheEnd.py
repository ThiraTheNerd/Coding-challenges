#MY ANSWER
def move_zeros(lst):
    #Count the number of zero's in the array.
    count = lst.count(0)
    print(lst.count(0))
    #Remove the zero's from the array
    while 0 in lst: lst.remove(0)
    print(lst)
    #Add the number of zeros found at the end of array
    zeros = [0] * count
    lst.extend(zeros)
    return lst


#CLEVER ANSWER
def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))