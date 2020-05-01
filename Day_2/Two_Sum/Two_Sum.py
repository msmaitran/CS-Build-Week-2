class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # build hash table/dictionary
        dict = {}
        # track the index of the value 
        for curr_index, num_1 in enumerate(nums):
            num_2 = target - num_1
            if num_2 not in dict:
                dict[num_1] = curr_index
            else:
                return [dict[num_2], curr_index]