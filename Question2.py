#A binary search function 

def binary_sort(sorted_list, length, key):
    start = 0
    end = length-1
    while start <= end:
        mid = int((start + end)/2)
        if key == sorted_list[mid]:
            print("\nEntered number %d is present at position: %d" % (key, mid))
            return -1
        elif key < sorted_list[mid]:
            end = mid - 1
        elif key > sorted_list[mid]:
            start = mid + 1
    print("\nNumber not found!")
    return -1
 
lst = []
 
#Size of lists

size = int(input("Enter size of list: \t"))
 
#Enter the numbers in the list

for n in range(size):
    numbers = int(input("Enter any number: \t"))
    lst.append(numbers)
 
lst.sort()
print('\n\nThe list is sorted, the sorted list is:', lst)
 
#Enter number to search
x = int(input("\nEnter the number to search: "))
 
binary_sort(lst, size, x)