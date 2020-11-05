# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：
#  
# 
#  
#  每次转换只能改变一个字母。 
#  转换过程中的中间单词必须是字典中的单词。 
#  
# 
#  说明: 
# 
#  
#  如果不存在这样的转换序列，返回 0。 
#  所有单词具有相同的长度。 
#  所有单词只由小写字母组成。 
#  字典中不存在重复的单词。 
#  你可以假设 beginWord 和 endWord 是非空的，且二者不相同。 
#  
# 
#  示例 1: 
# 
#  输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# 输出: 5
# 
# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
#      返回它的长度 5。
#  
# 
#  示例 2: 
# 
#  输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# 输出: 0
# 
# 解释: endWord "cog" 不在字典中，所以无法进行转换。 
#  Related Topics 广度优先搜索 
#  👍 554 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List


class Solution:
    def ladderLength(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        def addWord(word: str):
            if word not in word_id:
                nonlocal node_num
                word_id[word] = node_num
                node_num += 1

        def addEdge(word: str):
            addWord(word)
            id1 = word_id[word]

            chars = list(word)
            for i in range(len(chars)):
                tmp = chars[i]
                chars[i] = "*"
                new_word = "".join(chars)
                addWord(new_word)
                id2 = word_id[new_word]
                edge[id1].append(id2)
                edge[id2].append(id1)
                chars[i] = tmp

        word_id = dict()
        edge = collections.defaultdict(list)
        node_num = 0

        for word in word_list:
            addEdge(word)

        addEdge(begin_word)
        if end_word not in word_id:
            return 0

        dis_begin = [float("inf")] * node_num
        begin_id = word_id[begin_word]
        dis_begin[begin_id] = 0
        que_begin = collections.deque([begin_id])

        dis_end = [float("inf")] * node_num
        end_id = word_id[end_word]
        dis_end[end_id] = 0
        que_end = collections.deque([end_id])

        while que_begin or que_end:
            for _ in range(len(que_begin)):
                node_begin = que_begin.popleft()
                if dis_end[node_begin] != float("inf"):
                    return (dis_begin[node_begin] + dis_end[node_begin]) // 2 + 1
                for it in edge[node_begin]:
                    if dis_begin[it] == float("inf"):
                        dis_begin[it] = dis_begin[node_begin] + 1
                        que_begin.append(it)

            for _ in range(len(que_end)):
                node_end = que_end.popleft()
                if dis_begin[node_end] != float("inf"):
                    return (dis_begin[node_end] + dis_end[node_end]) // 2 + 1
                for it in edge[node_end]:
                    if dis_end[it] == float("inf"):
                        dis_end[it] = dis_end[node_end] + 1
                        que_end.append(it)
        return 0
    # leetcode submit region end(Prohibit modification and deletion)


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

print(Solution().ladderLength(beginWord, endWord, wordList))
