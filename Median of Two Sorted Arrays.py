def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
       #n-1 because indexing starts with zero
        if len(nums) % 2 == 0:                            # Median = 1/2{[(n/2)] + [(n/2+1)]}, if n is even. 
            return (nums[int(len(nums)/2 - 1)] + nums[int(len(nums)/2 + 1 - 1)])/2
        else:
            return nums[int((len(nums)+1)/2 -1)]          # Median = [(n+1)/2]th observation, if n is odd.
