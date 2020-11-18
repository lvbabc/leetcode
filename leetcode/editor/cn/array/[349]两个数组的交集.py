# 给定两个数组，编写一个函数来计算它们的交集。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2]
#  
# 
#  示例 2： 
# 
#  输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[9,4] 
# 
#  
# 
#  说明： 
# 
#  
#  输出结果中的每个元素一定是唯一的。 
#  我们可以不考虑输出结果的顺序。 
#  
#  Related Topics 排序 哈希表 双指针 二分查找 
#  👍 283 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        p1, p2 = 0, 0
        res = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
                while True:
                    if p1 < len(nums1) and nums1[p1] == nums1[p1-1]:
                        p1 += 1
                    else:
                        break
                while True:
                    if p2 < len(nums2) and nums2[p2] == nums2[p2-1]:
                        p2 += 1
                    else:
                        break
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return res
        
# leetcode submit region end(Prohibit modification and deletion)
num1 = [1,2,2,1]
num2 = [2,2]
print(Solution().intersection(num1, num2))