# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。 
# 
#  在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。 
# 
#  
# 
#  示例 1： 
# 
#  输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出：[[1,5],[6,9]]
#  
# 
#  示例 2： 
# 
#  输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出：[[1,2],[3,10],[12,16]]
# 解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
#  
# 
#  
# 
#  注意：输入类型已在 2019 年 4 月 15 日更改。请重置为默认代码定义以获取新的方法签名。 
#  Related Topics 排序 数组 
#  👍 253 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = newInterval
        placed = False
        res = []
        for li, ri in intervals:
            if li > right:
                if not placed:
                    res.append([left, right])
                    placed = True
                res.append([li, ri])
            elif ri < left:
                res.append([li, ri])
            else:
                left = min(li, left)
                right = max(ri, right)
        if not placed:
            res.append([left, right])
        return res
# leetcode submit region end(Prohibit modification and deletion)
