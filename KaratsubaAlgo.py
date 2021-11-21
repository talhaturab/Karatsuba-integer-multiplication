def main():
    x = "3141592653589793238462643383279502884197169399375105820974944592"
    y = "2718281828459045235360287471352662497757247093699959574966967627"
    ans = karatsuba(x, y)
    print(ans)
    

def karatsuba(x, y):
    if len(x) == 1 & len(y) == 1:
        return int(x) * int(y)

    else:
        # Matching the size of inputs
        if len(x) > len(y):
            for i in range(len(x) - len(y)):
                y = "0" + y

        if len(y) > len(x):
            for i in range(len(y) - len(x)):
                x = "0" + x

        # Making sure input is of even number
        if len(x) % 2 != 0:
            x = "0" + x
            y = "0" + y

        # a = "first half of x"
        a = x[:len(x)//2]
        
        # b = "second half of x"
        b = x[len(x)//2:]

        # c = "first half of y"
        c = y[:len(y)//2]

        # d = "second half of y"
        d = y[len(y)//2:]

        p = str(int(a) + int(b))
        q = str(int(c) + int(d))

        #compute ac, bd, pq
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        pq = karatsuba(p, q)
        
        #compute adbc
        adbc = pq - ac - bd

        return ((10**len(x)) * ac) + bd + ((10**(int(len(x)/2))) * adbc)

main()
