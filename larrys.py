# def larrysArray(A):
#     smallest = 1
#     while smallest < len(A)+1:
#         if A.index(smallest) != smallest - 1:
#             # print(A.index(smallest), smallest)
#             index = A.index(smallest)
#             # if index >= (len(A) - 2):
#             #     return 'NO'
#             small_array = select_items(A,index) 
#         smallest += 1

# # def check(index, arr):
# #     # comparison = A.index(smallest-1)
# #     # if (index - comparison) < 4:


# #     if arr[index-1]
# def select_items(arr, index):
#     high,low = 0,0
#     if arr[index-1] != 1:
#         if arr[index-2] != 1:
#             high,low = index+1,index-2
#         else:
#             high,low = index+2, index-1
#     else:
#         high,low = index+3,index
#     return arr[low:high]

x=[1,2,3,5,4]
# # print(select_items(x,1))


#do not put zero in selectitems

def larrysArray(A):
    total = 0
    for element in A:
        index, count = A.index(element), 0
        for item in A[:index+1]:
            if item > element:
                count += 1
        total += count
    if (total%2) == 0:
        return "YES"
    return "NO"
print(larrysArray(x))