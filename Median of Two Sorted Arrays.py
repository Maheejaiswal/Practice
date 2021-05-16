def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
       


Median = mean of (n/2)th observation and [(n/2)+1]th observation, if n is even.
        if len(nums) % 2 == 0:                            # Median = [(n/2)+1]th observation, if n is even.
            return (nums[int(len(nums)/2 - 1)] + nums[int(len(nums)/2 + 1 - 1)])/2
        else:
            return nums[int((len(nums)+1)/2 -1)]          # Median = [(n+1)/2]th observation, if n is odd.
