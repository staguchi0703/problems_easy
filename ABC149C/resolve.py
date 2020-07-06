def resolve():
    '''
    code here
    '''
    import math
    X = int(input())

    def is_prime(num):
        if num in [1, 2, 3]:
            return True
        else:
            div = 2
            while div <= int(math.sqrt(num)) + 1:
                if num % div == 0:
                    return False
                div += 1
            return True

    while is_prime(X) == False:
        X += 1

    print(X)

if __name__ == "__main__":
    resolve()
