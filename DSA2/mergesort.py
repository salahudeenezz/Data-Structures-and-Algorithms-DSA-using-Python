def merge_sort(arr):
    # check if length of the array is greater than 1
    if len(arr) > 1:
        # divide the length of the array by 2 to find the middle
        middle = len(arr) // 2

        # slice for left half from zero to the middle and slice for right half from middle to the end from the array
        left_half = arr[0:middle]
        right_half = arr[middle:]
         
        # recursively call the left half to divide and conquer and do the same for right half so we can merge it
        merge_sort(left_half)
        merge_sort(right_half)

        # create three variables and set all of them equal to zero -> i, j, and k
        i = 0
        j = 0
        k = 0

        # use i for the left_half and j for the right_half and k for the index of array to insert elements
        # use while loop to check if i is less than the left_half and check if j is less than the right_half
        # if it is then use the i as index for left_half and j for index for right_half to compare if left_half[i] is less than
        # right_half[j] and if yes then append it to the list as arr[k] = the left half[i] then increment i and k for that by 1
        # if it is greater but not less than, then make a else block and append the right_half and apply the same thing as before
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i = i + 1
                k = k + 1
            else:
                arr[k] = right_half[j]
                j += 1
                k += 1
        #create while loop for any value in left half left and right half.
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k = k + 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j = j + 1
            k += 1

    return arr  

print(merge_sort([5, 4, 3, 2, 1, 0]))