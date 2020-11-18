# 我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”： 
# 
#  
#  B.length >= 3 
#  存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B
# [B.length - 1] 
#  
# 
#  （注意：B 可以是 A 的任意子数组，包括整个数组 A。） 
# 
#  给出一个整数数组 A，返回最长 “山脉” 的长度。 
# 
#  如果不含有 “山脉” 则返回 0。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[2,1,4,7,3,2,5]
# 输出：5
# 解释：最长的 “山脉” 是 [1,4,7,3,2]，长度为 5。
#  
# 
#  示例 2： 
# 
#  输入：[2,2,2]
# 输出：0
# 解释：不含 “山脉”。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= A.length <= 10000 
#  0 <= A[i] <= 10000 
#  
#  Related Topics 双指针 
#  👍 116 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        start, max_length = 0, 0
        is_mountain = False
        length = len(A)
        for i in range(1, length - 1):
            # 当前处于下山
            if A[i - 1] > A[i] > A[i + 1]:
                if is_mountain and i == length - 2:
                    max_length = max(max_length, i - start + 2)
            # 当前处于山底
            if A[i - 1] > A[i] <= A[i + 1]:
                if is_mountain:
                    max_length = max(max_length, i - start + 1)
                    is_mountain = False
                start = i
            # 当前处于山顶
            if A[i - 1] < A[i] > A[i + 1]:
                is_mountain = True
                if i == length - 2:
                    max_length = max(max_length, i - start + 2)
            if A[i] == A[i - 1]:
                start = i
        return max_length
# leetcode submit region end(Prohibit modification and deletion)
