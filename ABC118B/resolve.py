def resolve():
    '''
    code here
    '''
    N, M = [int(item) for item in input().split()]
    As = [[int(item) for item in input().split()] for _ in range(N)]

    memo = [0 for _ in range(M+1)]

    for k, *items in As:
        for item in items:
            memo[item] += 1
    res = 0
    for item in memo:
        if item == N:
            res += 1

    print(res)


if __name__ == "__main__":
    resolve()
