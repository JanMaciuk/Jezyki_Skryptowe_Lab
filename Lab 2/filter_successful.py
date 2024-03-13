import sys

def filter_successful():
    for line in sys.stdin:
        try:
            if line.split()[-2] == '200':
                print(line)
        except:
            pass

if __name__ == '__main__':
    filter_successful()