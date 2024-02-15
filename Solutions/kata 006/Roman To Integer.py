#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        z = 0
        prev_value = 0
        
        for i in range(len(s) - 1, -1, -1):
            current_value = roman[s[i]]
            if current_value < prev_value:
                z -= current_value
            else:
                z += current_value
            prev_value = current_value
        
        return z

solution = Solution()
result = solution.romanToInt("MCMXCIV")
print(result)


# In[ ]:




