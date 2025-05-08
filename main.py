import random

array = []

array_len = input("Enter the length that the array will be: ")
if array_len == "--large-number-test":
    for i in range(0, 10000):
        array.append(random.randint(0, 10000))
else:
    for i in range(0, int(array_len)):
        num = int(input("Enter a number for the array: "))
        array.append(num)

def sort(arr):
    arr_len = len(arr)
    for i in range(arr_len):
        for j in range(0, arr_len - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

a = sort(array)
print(a)
