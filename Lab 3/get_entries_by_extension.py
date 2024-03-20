
def get_entries_by_extension(logs: list, extension: str) -> list:
    search_results = []
    for entry in logs:
        if entry[3].endswith(extension):
            search_results.append(entry)
    return search_results   # if extension is invalid, the list will be empty, no need for further validation

if __name__ == "__main__":
    from read_log import read_log
    logs = read_log()
    print(*get_entries_by_extension(logs, "jpeg"), sep='\n')