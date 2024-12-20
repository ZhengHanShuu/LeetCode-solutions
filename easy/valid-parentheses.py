# We will have a stack to store the opening bracket each time we went through
# the string, if it is the opening bracket, we will push it into the stack, if
# it is the closing bracket that is not corresponding to the closing bracket
# we will return false, if it is the closing bracket that corresponding to the
# closing bracket, we will pop it out of the stack. after the loop, if the stack
# is empty, we return true, otherwise false.


class Solution:
    def isValid(self, s: str) -> bool:
        # create an empty stack to store the opening bracket
        stack = []

        # create a hashmap to map the closing brackets to the opening brackets
        bracket_map = {
            ')': '(', '}': '{', ']': '['
        }

        # iterate through the string
        for char in s:
            if char in bracket_map:
            # pop from stack if there is a matching opening brackets
                top_element = stack.pop() if stack else '#'
                 # check if top of sstack matches the correct opeing brackets
                if bracket_map[char] != top_element:
                    return False
            else:
                # append it if it is a opening brackets
                stack.append(char)
        # return true if it is an empty stack
        return not stack