def resolve():
    '''
    code here
    '''
    import itertools
    N = int(input())
    P = tuple([int(item) for item in input().split()])
    Q = tuple([int(item) for item in input().split()])
    # print(Q)
    all = list(itertools.permutations(range(1,N+1)))
    a = 0
    b = 0
    for i, item in enumerate(all):
        # print(item)
        if item == P:
            a = i
        if item == Q:
            b = i

    print(abs(a-b))


if __name__ == "__main__":
    resolve()
