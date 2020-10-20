from typing import List


class Solution:
    def sortedSquares1(self, A: List[int]) -> List[int]:
        # 利用生成器和自带的TimSort，时间复杂度是O(N)
        return sorted([i**2 for i in A])

    def sortedSquares2(self, A: List[int]) -> List[int]:
        # 先排序再平方
        pass

    def sortedSquares3(self, A: List[int]) -> List[int]:
        # 因为原始数据是递增的，因此可以使用双指针，判断当abs(left)
        if A[0] >= 0:
            res = [i**2 for i in A]
        elif A[-1] <= 0:
            res = [i**2 for i in A[::-1]]
        else:
            res = [0] * len(A)
            left, right, cur = 0, len(A) - 1, len(A) - 1
            while left <= right:
                if abs(A[left]) > abs(A[right]):
                    res[cur] = A[left] ** 2
                    left += 1
                else:
                    res[cur] = A[right] ** 2
                    right -= 1
                cur -= 1
        return res

    def sortedSquares4(self, A: List[int]) -> List[int]:
        # 先找到正负数的分界线，然后双指针从中间到两端走，指针移动一次比较一次大小
        pass


if __name__ == "__main__":
    test_list = [-4,-1,0,3,10]
    test_list = [-4,-3,-2]
    print(Solution().sortedSquares3(test_list))
