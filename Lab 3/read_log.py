import sys
from datetime import datetime
# Każda linia logu zawiera:
# adres/nazwę hosta, który wykonywał żądanie,
# znacznik czasu w formacie "DAY/MON/YYY DD HH:MM:SS [TZ]",
# metodę protokołu HTTP wraz z ścieżką do żądanego zasobu,
# kod odpowiedzi HTTP (200 – w przypadku dostępności zasobu, 302 – zasób przeniesiony tymczasowo, 404 – gdy nie znaleziono),
# liczbę bajtów w odpowiedzi.
# Przykładowy log:
#199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245
#unicomp6.unicomp.net - - [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985

def read_log() -> list:
    logs = []
    for line in sys.stdin:
        try:
            line = line.split()
            host = line[0]
            time = line[3][1:]
            time = datetime.strptime(time, "%d/%b/%Y:%H:%M:%S")
            request_type = line[5][1:]
            resource_path = line[6]
            response_code = int(line[8])
            bytes = line[9]
            if bytes == '-':
                bytes = 0
            else:
                bytes = int(bytes)
            logs.append((host, time, request_type, resource_path, response_code, bytes))
            #Add a touple with all values to the logs list

        except: 
            # if errors on read or data type conversion occured, the line is improperly formatted, skip it.
            pass
    return logs


if __name__ == "__main__":
    read_log()