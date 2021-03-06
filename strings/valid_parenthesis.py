'''
brackets ="()", "{}", "[]"

input = "()" =>  true
input = "(())" => true
input = "(())[]" => true
input = "(())[])" => false

pseudocode
----------------------
create a function
stack
loop
check if current current character is "(", "{", "["
push to stack
else if current character is ")", "}", "]"
check if character at the top of stack is the openning racket for that specific element
return true, 
else return false


'''

def validparenthesis(s):
    if len(s) % 2 != 0 : return False

    bracketStack = []

    for i in range(len(s)):
        if s[i] == "(" or s[i] == "{" or s[i] == "[":
            bracketStack.append(s[i])
        elif s[i] == ")" and len(bracketStack) > 0:
            if bracketStack[len(bracketStack) - 1] == "(":
                bracketStack.pop()
                return True
            else: return False
        elif s[i] == "}" and len(bracketStack) > 0:
            if bracketStack[len(bracketStack) - 1] == "{":
                bracketStack.pop()
                return True
            else: return False
        elif s[i] == "]" and len(bracketStack) > 0:
            if bracketStack[len(bracketStack) - 1] == "[":
                bracketStack.pop()
                return True
            else: return False
        else: return False

output = validparenthesis("(){}}{")
print(output)
            



