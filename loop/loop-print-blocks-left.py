
def main():
    n = int(input('n = '))

    for i in range(n):
        for j in range(i + 1):
            for k in range(i + 1):
                if k < i:
                    print('0-', end = '')
                else:
                    print('0')

if __name__ == '__main__':
    main()