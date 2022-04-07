'''
Input: s = "[()]"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

pseudocode
-----------------
-Function(s)
-Check if len(s) % 2 != 0 return False
-Create a stack to track opening brackets
-loop through string s add opening brackets to stack
----if you encounter an opening bracket add to stack
----else if youbencounter a closing bracket, check if the the bracket at the top of the stack 
    is the correct opening bracket for the current clossing bracket, return true else return false
-return false outside the loop


'''

def isValid(s):
    if len(s) % 2 != 0: return False
    ourStack = []
    for currentCharacter in s:
        if currentCharacter == "(" or currentCharacter == "{" or currentCharacter == "[":
            ourStack.append(currentCharacter)
        elif currentCharacter == ")" and len(ourStack) > 0:
            if ourStack[len(ourStack) - 1] == "(" :
                ourStack.pop()
                return True
            else: return False
        elif currentCharacter == "}" and len(ourStack) > 0:
            if ourStack[len(ourStack) - 1] == "{":
                ourStack.pop()
                return True
            else: return False
        elif currentCharacter == "]" and len(ourStack) > 0:
            if ourStack[len(ourStack) - 1] == "[":
                ourStack.pop()
                return True
            else: return False

    return False
           
result = isValid("[()]")
print(result)


'''
time complexity = O(n)
space complexity = O(n)

'''


