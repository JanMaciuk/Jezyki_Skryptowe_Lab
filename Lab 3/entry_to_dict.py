
def entry_to_dict(entry) -> dict:
    return {
        "host": entry[0],
        "time": entry[1],
        "request_type": entry[2],
        "resource_path": entry[3],
        "response_code": entry[4],
        "bytes": entry[5]
    }

if __name__ == "__main__":
    from read_log import read_log
    logs = read_log()
    print(entry_to_dict(logs[0]))