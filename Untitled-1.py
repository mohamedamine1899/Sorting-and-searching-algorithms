def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_element = arr[i]
        j = i - 1

        while j >= 0 and current_element < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = current_element
my_array = [12, 11, 13, 5, 6]
insertion_sort(my_array)
print("Sorted array is:", my_array)


