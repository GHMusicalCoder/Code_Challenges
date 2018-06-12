class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(x ** 0.5)


x = Solution()
print(x.mySqrt(9))
print(x.mySqrt(183))