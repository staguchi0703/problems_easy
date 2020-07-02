def resolve():
    '''
    code here
    '''
    N = int(input())
    res = 0

    def div2(num):
        if num == 1:
            return 0
        else:
            cnt = 0
            while True:
                if num % 2 == 0:
                    num //= 2
                    cnt += 1
                else:
                    return cnt


    res_max_cnt = 0
    res = 1
    for i in range(N):
        tepm_cnt = div2(i+1)
        if res_max_cnt < tepm_cnt:
            res_max_cnt = tepm_cnt
            res = i+1
    print(res)

if __name__ == "__main__":
    resolve()
