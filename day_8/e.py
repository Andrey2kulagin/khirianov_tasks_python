# короче новую строку буду делать из кусочков+ пробел, н всегда менять

def is_True(inp):
    for i in range(len(inp)-1):
        if inp[i]=='('and inp[i+1]!='(':
            r_index = inp.index(')')+1
            inp = inp[0:i]+" "+inp[r_index::]
            cure_str = inp[i+1:r_index]
            print(cure_str)
            for j in range(len(cure_str)):
                if cure_str[j] not in(')',''):
                    return False
        print(inp)
        is_True(inp)

inp = input()
n = len(inp)
flag = True if inp.count('(')!=0 else False
is_True(inp)
    