"""Write a python program to store first year percentage of students in array. Write
function for sorting array of floating point numbers in ascending order using
quick sort and display top five scores."""

arr =[]
def percentage():
    n=int(input("Enter number of students: "))
    for i in range(n):
        i==0
        i=i+1
        print("Enter percentage of student",i,":")
        ele=float(input())
        arr.append(ele)
    print("marks of students are:",arr)
percentage()
def quicksort(arr,left,right):
    if left < right:
        partition_pos = partition(arr, left , right)
        quicksort(arr, left,partition_pos-1 )
        quicksort(arr,partition_pos+1, right )
        
def partition(arr, left ,right):
    i = left
    j = right -1
    pivot = arr[right] 

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j :
            arr[i], arr[j] = arr[j], arr[i]
    
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    
    return i

quicksort(arr, 0, len(arr)-1)
print(f'\nSorted array: {arr}')

def top_fivescores():
    print("\nThe top five sccores are:",arr[-1:-6:-1])
top_fivescores()