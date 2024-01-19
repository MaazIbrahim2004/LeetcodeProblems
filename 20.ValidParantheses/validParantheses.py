class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {")": "(", "]" : "[", "}" : "{"}  # key is closed, value is open
        for char in s:
            if char in dict:  # check if it's a closing parenthesis(key)
                if stack and stack[-1] == dict[char]:  # if stack not empty and front of stack is an open parenthesis
                    stack.pop()
                else:
                    return False # cuz then not same parantheses for open
            else:
                stack.append(char) # if its not in key, its an open parantheses, so add it to stack
        return True if not stack else False  # return True if stack is not empty, otherwise False
