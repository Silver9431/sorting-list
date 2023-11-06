def selection_sort(arr):
    x = len(arr)
    for i in range(x):
        min_idx = i
        for y in range(i + 1, x):
            if arr[y] < arr[min_idx]:
                min_idx = y
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

my_list = [31, 94, 51, 88, 22]
selection_sort(my_list)

print("Sorted array is:", my_list)