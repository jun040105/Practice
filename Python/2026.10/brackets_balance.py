def check_balance(brackets):

    count = 0 

    for i in brackets:

        if i == "(":
            count += 1
        if i == ")":
            count -= 1

        if count < 0:
            return False

    if count == 0:
        return True
    else:
        return False