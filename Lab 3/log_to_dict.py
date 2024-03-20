from entry_to_dict import entry_to_dict

def log_to_dict(logs: list) -> dict:
    result_dict: dict = {}
    for entry in logs:
        result_dict[entry[0]] = entry_to_dict(entry)
    return result_dict

if __name__ == "__main__":
    from read_log import read_log
    logs = read_log()
    result = log_to_dict(logs)
    for key in result:
        print(f"{key}: {result[key]}\n")