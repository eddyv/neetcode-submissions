class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = { ')': '(', "}": "{", "]": "["}
        
        for letter in s:
            
            if letter in brackets.values():
                stack.append(letter)
            else:
                if len(stack) == 0:
                    return False
                popped_letter = stack.pop()
                if popped_letter != brackets[letter]:
                    return False
        if len(stack) > 0:
            return False
        return True

        