
def get_failed_reads(logs: list, joinLists: bool = False) -> list:
    logs400 = []
    logs500 = []
    for line in logs:
        try:
            if line[4] >= 400 and line[4] < 500:
                logs400.append(line)
            elif line[4] >= 500 and line[4] < 600:
                logs500.append(line)
        except:
            pass # Comparison failed or line doesn't have 4th index, either way a bad format, skip

    if joinLists:
        return logs400 + logs500
    else:
        return logs400, logs500
    
if __name__ == "__main__":
    from read_log import read_log
    logs = read_log()
    print(*get_failed_reads(logs, True), sep='\n')
        