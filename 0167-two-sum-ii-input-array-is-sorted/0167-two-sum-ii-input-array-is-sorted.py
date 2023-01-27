class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        
        while(1):
            my_target = target - numbers[i]
            
            # do binary search for my_target (givem numbers are sorted)
            low = i + 1
            high = len(numbers) - 1
            while(low <= high):
                center = (low + high) // 2
                if numbers[center] == my_target:
                    return [i+1, center+1]
                elif numbers[center] > my_target:
                    high = center - 1
                else:
                    low = center + 1
            
            
            i += 1
        
        
        