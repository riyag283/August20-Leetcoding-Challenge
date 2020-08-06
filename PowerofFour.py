class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        num = "{0:b}".format(num)
        size = len(num)
        if size%2 == 0:
            return False
        else:
            if '1' in num[1:]:
                return False
            else:
                return True
