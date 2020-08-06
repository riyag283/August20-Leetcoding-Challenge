class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is '':
            return True
        s = s.lower()
        l, h = 0, len(s)-1
        while l <= h:
            #print(s[l],s[h])
            if not s[l].isalnum():
                l += 1
            elif not s[h].isalnum():
                h -= 1
            elif s[l] == s[h]:
                l += 1
                h -= 1
            else:
                return False
        return True
