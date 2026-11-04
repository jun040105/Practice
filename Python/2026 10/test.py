def well_formed(line):    

    stack = []

    for i in line:
      
      if i in "({[":
        stack.append(i)  
      else:
        if not stack:
          return False

        a = stack.pop()
        
        if i == ")" and a == "(":
          pass
        elif i == "]" and a == "[": 
          pass
        elif i == "}" and a == "{": 
          pass
        else: return False

    return len(stack) == 0
