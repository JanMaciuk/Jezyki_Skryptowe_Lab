import sys
def count_codes():
    code200 = 0
    code302 = 0
    code404 = 0
    for line in sys.stdin:
        code200 += line.count('200')
        code302 += line.count('302')
        code404 += line.count('404')
    print('200:', code200)
    print('302:', code302)
    print('404:', code404)

if __name__ == '__main__':
    count_codes()