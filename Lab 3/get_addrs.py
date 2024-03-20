
def get_addrs(logs: dict) -> list:
    return list(set(logs.keys()))   # set in order to avoid duplicates

if __name__ == "__main__":
    from read_log import read_log
    from log_to_dict import log_to_dict
    logs = read_log()
    result = log_to_dict(logs)
    print(get_addrs(result))