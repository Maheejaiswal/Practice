#reverse an array

def reverse_array(arr):
  return arr[::-1]

arr = [1,2,3,4,5,6]
print("Before reversing: ", arr)
arr1 = reverse_array(arr)
print("After reversing:", arr1)
