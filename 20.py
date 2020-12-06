class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')', '[':']', '{':'}','a':'a'}
        stack = ['a']
        for i in s:
            if i in dic:
                stack.append(i)
            elif dic[stack.pop()] != i:
                return False
