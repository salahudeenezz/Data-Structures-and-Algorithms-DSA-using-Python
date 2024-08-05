def selection_sort(numbers):
    n = len(numbers)
    for i in range(0, n-1):
        minimum = i 
        for j in range(i+1, n):
            if numbers[i] > numbers[j]:
                minimum = j
        if numbers[minimum] < numbers[i]:
            temp = numbers[i]
            numbers[i] = numbers[minimum]
            numbers[minimum] = temp
    return numbers




result = selection_sort([5, 4, 3, 2, 1])
print(result)