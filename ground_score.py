# def multiple_of_five(num):
#     if (num+1) % 5 == 0 or (num+2) % 5 == 0:
#         return True
#     return False

# print(multiple_of_five(6))

def kaprekarNumbers(p,q):
    x = ''
    for i in range(p,q):
        square = i*i
        if i == 1:
            x+= str(i)       
        mid_point = len(str(square)) // 2
        if mid_point >= 1:
            l = str(square)[:mid_point]
            r = str(square)[mid_point:]
            sum = int(l) + int(r)
            if sum == i:
                x += str(i)
    print(x)
            

print(kaprekarNumbers(1,10))