import sys

def graphics_rate():
    graphics = 0
    other = 0
    for line in sys.stdin:
        if 'gif' in line or 'jpg' in line or 'jpeg' in line or 'xbm' in line:
            graphics += 1
        else:
            try:
                if line.split()[-2] == '200':
                    other += 1  # 200 code means the request was successful, don't count failed requests
            except:
                pass
    print('Graphics downloads to other downloads rate: ', graphics/other)

if __name__ == '__main__':
    graphics_rate()
