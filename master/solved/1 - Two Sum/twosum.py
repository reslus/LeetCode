from typing import List

class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        """This isn't my original code. It works really fast though. 
           I understand it now. See NOTE: below."""
        hashmap = {}
        for i, in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i

    @staticmethod
    def twoSum_v2(nums: List[int], target: int) -> List[int]:
        """Improvement to above function."""
        hashmap = {}  # Key: Number, Value: Index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[num] = i

    @staticmethod
    def twoSum_v3(nums: List[int], target: int) -> List[int]:
        """My attempt to see if I can improve the above code."""
        hashmap = dict(zip(range(len(nums)), nums))
        
        return None


if __name__ == "__main__":
    # print(Solution.twoSum(nums=[2,7,11,15,22], target=34))
    print(Solution.twoSum_v2(nums=[2,7,11,15,22], target=33))



# NOTE: 
    # this is how I understand this to work
    # it loops thru each element in nums and calculates the complement (target - element)
    # on every iteration, it checks to see if the complement exists in hashmap, if it does, it has found the two pairs
    # if it doesn't, it adds {element, iterator} to hashmap's growing dict.