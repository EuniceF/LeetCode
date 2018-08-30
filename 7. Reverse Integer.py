class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            n = int(str(x)[::-1])
        else:
            n = int(str(x*(-1))[::-1])
            n = n * (-1)
        # use built-in function: bit_length()
        if n.bit_length() < 32: 
            return n
        else:
            return 0
