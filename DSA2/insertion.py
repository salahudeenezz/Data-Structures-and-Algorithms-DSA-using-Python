def insertion_sort(numbers):
    n = len(numbers)
    for i in range(1, n):
        j = i
        while numbers[j-1] > numbers[j] and j > 0:
            numbers[j-1], numbers[j] = numbers[j], numbers[j-1]
            j = j - 1
    
    return numbers



result = insertion_sort([5, 4, 3, 2, 1])
print(result)