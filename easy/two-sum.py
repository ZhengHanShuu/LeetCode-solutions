#Problem: Two Sum


#Brute force:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)):
            for j in range (i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        # return empty list if no solution is found
        return []

# hash map:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hashmap
        hashmap = {}
        # iterate through the list of the nums, start from i
        for i in range (len(nums)):
            # check if there is a number that is equal to the target - nums[i]
            complement = target - nums[i]
            # if the complement is in hashmap return the nums[i] and the number
            # that is equal to target - nums [i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            # the nums[i] is store to the hashmap if the complement is not found yet
            hashmap[nums[i]] = i
        # return an empty list if not found solution
        return []
