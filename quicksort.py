"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
# def quicksort(array):
#     sorted_array=[0]*len(array)
#     if len(array) == 1:
#         return array
#     if len(array) < 1:
#         return "Error"
#     pivot = sort_array(array, sorted_array)

    
    
    
#     # # print(array[:index])
#     # # print(array[index + 1:])
#     if pivot == array[index]:
#         return quicksort(array[:index])
#     return sorted_array
    
# def sort_array(array, sorted_array):
#     pivot = array[-1]
#     index = 0
#     pivot_index = -1
#     while index < array.index(pivot):
#         pivot = array[pivot_index]
#         if array[index] > pivot:
#             array[pivot_index] = array[index]
#             array[index] = array[pivot_index - 1]
#             pivot_index -= 1
#             array[pivot_index] = pivot
#         else:
#             index += 1
#     sorted_array[index] = pivot
#     return pivot



"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def partition(arr,low,high): 
    # print arr
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high)
    return arr
        
def quicksort(array):
    n = len(array)
    return quickSort(array,0,n-1)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)