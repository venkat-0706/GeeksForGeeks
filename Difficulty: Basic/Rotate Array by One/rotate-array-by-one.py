from typing import List

class Solution:
    def rotate(self, arr: List[int]) -> List[int]:
        n = len(arr)
        temp = arr[n - 1]    
        for i in range(n - 1, 0, -1): 
            arr[i] = arr[i - 1]
        arr[0] = temp         
        return arr
