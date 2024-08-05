def bubble_sort(numbers):
    n = len(numbers) 
    for i in range(0, n-1):
        for j in range(0, n-1):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp
    return numbers

numbers = bubble_sort([5, 4, 3, 2, 1])
print(numbers)