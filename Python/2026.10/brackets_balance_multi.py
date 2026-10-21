def multi_bracket(brackets):

    stack = []

    for i in brackets:

        if i in "([{":
            stack.append(i)

        else: 

            if not stack: 
                return False

            x = stack.pop()

            if x == "(" and i == ")": pass
            elif x == "[" and i == "]": pass
            elif x == "{" and i == "}": pass
            else: return False

    return len(stack) == 0 
    


