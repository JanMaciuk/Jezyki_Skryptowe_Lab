import sys

def count_bytes():
    byte_count = 0
    for line in sys.stdin:
        try:
            bytes = line.split()[-1]
            if bytes.isdigit():
                byte_count += int(bytes)
        except:
            pass

    print("Total data transfered in GB: " + str(byte_count*0.000000001))   # Convert to gigabytes

if __name__ == '__main__':
    count_bytes()