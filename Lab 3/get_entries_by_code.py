def get_entries_by_code(logs: list, code: int) -> list:
    allowed_codes = (200, 302, 404)
    if not allowed_codes.__contains__(code):
        raise ValueError("Queried code is not supported or is invalid")
    search_results = []
    for entry in logs:
        if entry[4] == code:
            search_results.append(entry)
    return search_results   # if an inserted adress is incorrect or hasn't made any requests, the list will be empty, no need for further validation

if __name__ == "__main__":
    from read_log import read_log
    logs = read_log()
    print(*get_entries_by_code(logs, 302), sep='\n')