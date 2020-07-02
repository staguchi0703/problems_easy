def resolve():
    '''
    code here
    '''
    import math
    a, b =input().split()

    temp = int(a+b)

    if (int(math.sqrt(temp)))**2 == temp:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    resolve()
