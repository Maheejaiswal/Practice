# Given a sorted array (ascending order) and a target number, find the first index of this number in O(log n)O(logn) time complexity.
# If the target number does not exist in the array, return -1

def binarySearch(self, nums, target):
        # write your code here
        if target in nums:
            return nums.index(target) 
        else:
            return -1
