#!/usr/bin/env python
# coding: utf-8

# In[1]:


from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0                                          #initialize result variable to store result
        for nums in nums:                                   #read each element in array
            result ^= nums                                  #XOR the element in array
        return result
nums = [4, 2, 1, 2, 1]
solution = Solution()
print(solution.singleNumber(nums))


# In[ ]:




