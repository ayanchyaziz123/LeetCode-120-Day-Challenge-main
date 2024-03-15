#Leetcode problem:-> 1. Two Sum
#Ayan's code
class Map:
    def __init__(self, key: int, val: int) -> None:
      self.key= key
      self.val= val
    def get_val(self):
      return self.val  
class Solution():
    def __init__(self) -> None:
      self.arr = []
    #Time Complexity: 0(n)  
    def twoSum_n(self, nums: list[int], target: int) -> list[int]:
       num_map = {}
       for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_map:
                return [num_map[complement], i]
            num_map[nums[i]] = i
       return None
    
    # Time Complexity: 0(nlogn) 
    def twoSum_nlogn(self, nums: list[int], target: int) -> list[int]:
        for i in range(0, len(nums)):
         self.arr.append(Map(i, nums[i]))
        self.arr.sort(key=lambda x: x.get_val()) 
        left, right = 0, len(nums) - 1
        while(left < right):
          sum = self.arr[left].val + self.arr[right].val
          if sum == target:
            return [min(self.arr[left].key, self.arr[right].key), max(self.arr[left].key, self.arr[right].key)]
          elif sum < target:
            left += 1
          else:
            right -= 1
        return None    
    
    # Time Complexity: 0(n^2)      
    def twoSum_n2(self, nums: list[int], target: int) -> list[int]:
        for i in range(0, len(nums)):
           for j in range(i + 1, len(nums) - 1):
              if (nums[i] + nums[j]) == target:
                 return [i, j] 
        return None                 
sl = Solution()
arr=[10, 20, 30, 9, 3, 7]
# 3 7 9 10 20 30
print(sl.twoSum_nlogn(arr, 29))