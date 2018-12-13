# -*- coding: utf-8 -*-

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        result = 0
        begin = 0
        end = 0
        cursor = 0
        characters = {}
        
        for index, value in enumerate(s):
            if value in characters:
                cursor = characters[value]
                
                '''be careful when update the index 'begin' '''
                if begin <= cursor:
                    begin = cursor + 1
            
            length = end - begin + 1
            if length > result:
                result = length
            
            characters[value] = index
            end = end + 1
            
        return result
    
    def test_solution():
        s = Solution()
        str = "abcadcbb"
        
        assert(s.lengthOfLongestSubstring(str) == 3)