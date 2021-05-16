def binary_search(arr,low,high,x):
    
    if high >= low:
        mid =(high + low)// 2
        
        if arr[mid] > x:
            return binary_search(arr,low,mid-1,x)
            
        elif arr[mid] < x:
            return binary_search(arr,mid+1,high,x)
            
        else:
            return mid
            
    else:
        return 1
        
arr = [0,1,2,3,4,5]

result = binary_search(arr,0,len(arr)-1,4)

if result != 1:
    print(result)
    
else:
    print("sorry")
