#==== ASCENDING ORDER With min() and max() function ===============



# sort(): build in list method
# sorted(): build in function


def swap_first_last(list1):
    minimum_value = min(list1)
    #print(minimum_value) # 0
    minimun_index = list1.index(minimum_value)# index of 0 in the list is 5

    # here we swap the first and last index 
    list1[0], list1[minimun_index] = list1[minimun_index], list1[0]
    #first part is variables = values   
    return list1

#print(swap_first_last([56, 3, 2, 78, 6, 0]))
#[0, 3, 2, 78, 6, 56]  3, 2, 78, 6, will be unsorted elements



#=========== To Sorted others elements we need for loop  bcz there a lot ============

def order_list(list1):
    for i in range (len(list1)):
        minimum_value = min(list1[i:])
        minimun_index = list1.index(minimum_value) 
        list1[i], list1[minimun_index] = list1[minimun_index], list1[i]

    return f"The value in order list is : {list1}"

print(order_list([56, 3, 2, 78, 6, 0]))