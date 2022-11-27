def findDigitSum(n, b, s):
    '''
    n - integer, next n numbers.
    b - integer, base between 2 and 9 inclusively.
    s - integer, the start number.
    '''

    # convert s (base b) into decimal
    # d = 0 # the decimal number for s
    # for x in str(s):
    #     d = d * b + int(x)
    # print('decimal of s:', d)

    # generate next n numbers from s, and convert it to base b
    total = 0
    nums = []
    for x in range(n):
        s1 = s + x
        nums.append(s1)
        # convert to base b
        while s1:
            total = total + s1 % b
            s1 = s1 // b
    print('next %d numbers: %s' % (n, nums))
    print('the sum of digits of all generated numbers:', total)

    return total

findDigitSum(15, 8, 2)
findDigitSum(15, 8, 12)
findDigitSum(5, 7, 15)
