import sys

def filter_poland():
    for line in sys.stdin:
        try:
            host = line.split()[0]
            if host[len(host)-3:len(host)] == '.pl':
                print(line)
        except:
            pass

if __name__ == '__main__':
    filter_poland()