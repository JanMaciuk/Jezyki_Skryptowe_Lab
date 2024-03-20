
def get_entries_by_addr(logs: list, host: str) -> list:
    search_results = []
    for entry in logs:
        if entry[0] == host:
            search_results.append(entry)
    return search_results   # if an inserted adress is incorrect or hasn't made any requests, the list will be empty, no need for further validation

if __name__ == "__main__":
    from read_log import read_log
    logs = read_log()
    print(*get_entries_by_addr(logs, '199.72.81.55'), sep='\n')