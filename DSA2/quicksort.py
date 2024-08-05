def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
    
    less_than_the_pivot = []
    greater_then_the_pivot = []
    
    for item in arr:
        if item > pivot:
            greater_then_the_pivot.append(item)
        else:
            less_than_the_pivot.append(item)
    
    return quick_sort(less_than_the_pivot) + [pivot] + quick_sort(greater_then_the_pivot)
    

print(quick_sort([6,5,3,2,4]))