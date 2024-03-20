
def sort_log(logs: list, elementIndex: int):
    try:
        logs.sort(key=lambda x: x[elementIndex])
        return logs
    except Exception as e:
        # not sure whats the point of catching this exception, 
        # just throwing it seems appropriate,
        # cannot continue with wrong logs or index.
        raise e 


if __name__ == "__main__":
    from read_log import read_log
    logs = read_log()
    print(sort_log(logs,1))
    print(sort_log(logs,2))
    print(sort_log(logs,3))
    print(sort_log(logs,4))
    print(sort_log(logs,5))