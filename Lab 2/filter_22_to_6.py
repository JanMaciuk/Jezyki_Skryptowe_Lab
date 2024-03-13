import sys

def filter_22_to_6():
    for line in sys.stdin:
        try:

            time = line.split()[3][13:15]   # Extract the hour from the time field
            if time.isdigit():
                time = int(time)
                if time < 6 or time > 22:
                    print(line)
        except:
            pass

if __name__ == '__main__':
    filter_22_to_6()