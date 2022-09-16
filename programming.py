#1. Write a Python Program to find sum of array?


arr =[]
arr =[1,3,4,6,7,8,5,7,9,7,8,9]


ans = sum(arr)

print("the sum of the array is : ", ans)

#2. Write a Python Program to find largest element in an array?



arr = [23, 55, 34, 65, 78, 90, 10, 23, 45, 67, 32, 87, 90]
n = len(arr)


def largest(arr, n):
    max = arr[0]

    for i in range(1, n):
          if max < arr[i]:
              max = arr[i]
    return max

q = largest(arr,n)

print("the largest array number is", q)



#3. Write a Python Program for array rotation?


arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def rotate(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr


print("Array after left rotation is: ", end=' ')
print(rotate(arr, len(arr), 2))


#4. Write a Python Program to Split the array and add the first part to the end?


my_list = eval(input("Enter the array:  " ))

def split(list_a, chunk_size):

  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]

chunk_size = 2

print(list(split(my_list, chunk_size)))
print("the sum of last two arry is: ", my_list[0] + my_list[-1] )

#5. Write a Python Program to check if given array is Monotonic ?


def checkMonotonic():
    in_arr = eval(input("Enter the Array: "))
    if(all(in_arr[i]<=in_arr[i+1] for i in range(len(in_arr)-1)) or all(in_arr[i]>=in_arr[i+1] for i in range(len(in_arr)-1))):
        print(f'Array {in_arr} is Monotonic')
    else:
        print(f'Array {in_arr} is Not Monotonic')

checkMonotonic()
checkMonotonic()
