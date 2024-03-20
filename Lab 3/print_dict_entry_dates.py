from get_addrs import get_addrs
from datetime import datetime

def print_dict_entry_dates(logs: dict) -> None: # function's name is misleading, it does many things, and not really focused on dates
    
    def get_all_values_of_key(dictionary, key):
        values = []
        for k, v in dictionary.items():
            if k == key:
                values.append(v)
        return values

    hosts = get_addrs(logs)
    for host in hosts:
        request_count = 0
        earliest_entry = datetime.max
        latest_entry = datetime.min
        code_200_requests = 0

        for entry in get_all_values_of_key(logs, host): 
            request_count += 1
            if entry["time"] < earliest_entry:
                earliest_entry = entry["time"]

            if entry["time"] > latest_entry:
                latest_entry = entry["time"]

            if entry["response_code"] == 200:
                code_200_requests += 1
        print(
            "\nHost adress: " + str(host) + ", total requests made: " + str(request_count) + 
            ", first request made on: " + str(earliest_entry) + ", last request made on: " + str(latest_entry) +
            ", ratio of succesfull requests to all requests:" + str(code_200_requests/request_count)
        )

if __name__ == "__main__":
    from read_log import read_log
    from log_to_dict import log_to_dict
    logs = read_log()
    result = log_to_dict(logs)
    print_dict_entry_dates(result)
            
        
        