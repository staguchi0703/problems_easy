def resolve():
    '''
    code here
    '''
    S = input()
    res = 0
    max_res = 0
    for i in range(len(S)):
        if S[i] in ['A', 'C', 'G', 'T']:
            res += 1
        else:
            res = 0
        max_res = max(max_res, res)
    print(max_res)
if __name__ == "__main__":
    resolve()
