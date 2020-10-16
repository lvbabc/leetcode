# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。 
# 
#  你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = [1]
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目在范围 [0, 100] 内 
#  0 <= Node.val <= 100 
#  
#  Related Topics 链表 
#  👍 716 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # if not head or not head.next:
        #     return head
        # next_node = head.next
        # head.next = self.swapPairs(next_node.next)
        # next_node.next = head
        # return next_node
        dummy_head = ListNode(0, head)
        tmp = dummy_head
        while tmp.next and tmp.next.next:
            node1 = tmp.next
            node2 = tmp.next.next

            tmp.next = node2
            node1.next = node2.next
            node2.next = node1
            tmp = node1
        return dummy_head.next

# leetcode submit region end(Prohibit modification and deletion)
