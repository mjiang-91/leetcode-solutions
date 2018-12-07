class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        
        def backtrace(S='', left=0, right=0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            
            if left < n:
                backtrace(S+'(', left + 1, right)
            if right < left:
                backtrace(S+')', left, right + 1)
            
        backtrace()
        
        return ans

def test_solution():
    ss = Solution()
    expected = ["((()))","(()())","(())()","()(())","()()()"]
    
    assert expected == ss.generateParenthesis(3)
