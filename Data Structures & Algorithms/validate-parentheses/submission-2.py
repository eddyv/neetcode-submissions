class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for letter in s:
            if letter == '(' or letter == '[' or letter == '{':
                stack.append(letter);
            else:
                if len(stack) == 0:
                    return False
                popped_letter = stack.pop();
                if letter == ')' and popped_letter == '(':
                    continue
                elif letter == ']' and popped_letter == '[':
                    continue
                elif letter == '}' and popped_letter == '{':
                    continue
                else:
                    return False
            print(f"stack: {stack}")

        if len(stack) > 0:
            return False
        return True

        