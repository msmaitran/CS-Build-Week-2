class Solution {
    fun containsDuplicates(nums: IntArray): Boolean {
        return nums.size != nums.distinct().count()
    }
}