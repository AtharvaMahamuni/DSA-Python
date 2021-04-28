class Solution:

    def ispar(self, expr):

        stack = []
        for char in expr:
            if char in ['(', '[', '{']:
                stack.append(char)
            else:
                if char == ')':
                    if stack.pop() != '(':
                        return False
                elif char == ']':
                    if stack.pop() != '[':
                        return False
                elif char == '}':
                    if stack.pop() != '{':
                        return False

        # This condition to check whether there is an element present in a stack or not
        # If there is an element return False
        if stack:
            return False
        return True


s = Solution()

par = input()

print(s.ispar(par))
