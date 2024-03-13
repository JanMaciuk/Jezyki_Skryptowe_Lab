import sys

def biggest_resource():
    max_bytes = 0
    max_resource = ''
    for line in sys.stdin:
        try:
            bytes = line.split()[-1]
            if bytes.isdigit():
                bytes = int(bytes)
                if bytes > max_bytes:
                    max_bytes = bytes
                    max_resource = line.split()[6]
        except:
            pass
    print("Path to biggest resource: " + max_resource)
    print("Biggest resource size in bytes: " + str(max_bytes))

if __name__ == '__main__':
    biggest_resource()