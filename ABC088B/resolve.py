def resolve():
    '''
    code here
    '''
    N = int(input())
    As = [int(item) for item in input().split()]
    As = sorted(As)

    turn = 0
    A = 0
    B = 0
    while As:
        if turn % 2 == 0:
            A += As.pop()
        else:
            B += As.pop()

        turn += 1
    print(A-B)




if __name__ == "__main__":
    resolve()
