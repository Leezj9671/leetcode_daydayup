"""
1. 第一位或最后一位不一样就是错误的
2. 相同则递增
3. 如果name和typed对比不同，那么这个字符和上个字符相同的话略过
4. 如果name_cur到len(name)则
5. 如果都不是，说明没匹配上，浮标回到0
"""

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name == typed:
            return True
        if name[0] != typed[0] or name[-1] != typed[-1]:
            return False
        name_cur = 0
        for index, typed_char in enumerate(typed):
            if name_cur == len(name):
                break
            if name[name_cur] == typed_char:
                name_cur += 1
            elif typed[index] == typed[index-1]:
                continue
            else:
                name_cur = 0
        if name_cur == len(name):
            return True
        return False


assert Solution().isLongPressedName('laiden', 'laiden') is True
assert Solution().isLongPressedName('alex', 'aaleexxr') is False
assert Solution().isLongPressedName('alex', 'aaleex') is True
assert Solution().isLongPressedName('saeed', 'ssaaedd') is False
assert Solution().isLongPressedName('leelee', 'lleeelee') is True
assert Solution().isLongPressedName('kikcxmvzi', 'kiikcxxmmvvzz') is False
assert Solution().isLongPressedName('vtkgn', 'vttkgnn') is True
assert Solution().isLongPressedName('saeedi', 'ssaaeediixxxiii') is True
assert Solution().isLongPressedName('zlexya', 'aazlllllllllllllleexxxxxxxxxxxxxxxya') is False
