def insertion_sort(list_a):
    indexing_length = range(1, len(list_a))

    for i in indexing_length:
        value_to_sort = list_a[i]

        while list_a[i-1] > value_to_sort and i>0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i = i-1
        
    return list_a
    
print(insertion_sort([1,2,1,1,4,3,5,6,9,3,3,2,1]))