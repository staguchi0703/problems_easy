def resolve():
    '''
    code here
    '''
    S = input()

    front = -1
    end = 0
    for i in range(len(S)):
        if S[i] in ['A', 'C', 'G', 'T']:
            front = i
            break

    for i in range(len(S)):
        if S[-1*(i+1)] in ['A', 'C', 'G', 'T']:
            end = i
            break
    if front == -1:
        print(0)
    elif front == len(S) -1 - end:
        print(1)
    else:
        print(len(S) - end - front)

if __name__ == "__main__":
    resolve()
