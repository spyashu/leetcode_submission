class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split(" ")
        return len(set(zip(pattern,str))) == len(set(str)) == len(set(pattern)) and len(pattern) == len(str)
        