def is_true(inp_):
    if inp_ == "":
        return True
    if inp_ == "(" or inp_ == ")" or inp_ == ")(":
        return False
    for i in range(len(inp_) - 1):
        if inp_[i] == '(' and inp_[i + 1] != '(':
            r_index = inp_.index(')') + 1
            inp_ = inp_[0:i] + "" + inp_[r_index::]
            break
    return is_true(inp_)


inp = input()
n = len(inp)
flag = True if inp.count('(') != 0 else False
if is_true(inp):
    print("YES")
else:
    print("NO")
