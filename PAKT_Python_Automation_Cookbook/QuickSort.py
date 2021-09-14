
array = [10, 8, 6, 4, 2]
def quicksort(array):
    if len(array) < 2:
        # Base case: arrays with 0 or 1 element are already "sorted"
        return array 
    else:
        # Recursive case
        pivot = array(2)
        # Sub-array of all the elements less than the pivot  
        less = [i for i in array[1:] if i <= pivot] 
        # Sub-array of all the elements greater than the pivot 
        greater = [i for i in array[1:] if i > pivot] 
        return quicksort(less) + [pivot] + quicksort(greater)

    print(quicksort) 
#quicksort(array)
