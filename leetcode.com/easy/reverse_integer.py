class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp = int(str(abs(x))[::-1])
        if x < 0:
            temp *= -1
        return temp if -2147483648 <= temp <= 2147483647 else 0


x = Solution()
print(x.reverse(123))
print(x.reverse(1534276869))