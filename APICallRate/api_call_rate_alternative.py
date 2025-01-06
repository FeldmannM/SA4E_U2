import http.client
import time

def measure_api_calls_per_second(host, endpoint, duration):
    start_time = time.time()
    count = 0

    while time.time() - start_time < duration:
        connection = http.client.HTTPConnection(host)
        connection.request("GET", endpoint)
        response = connection.getresponse()
        if response.status == 200:
            count += 1
        connection.close()

    elapsed_time = time.time() - start_time
    return count / elapsed_time

if __name__ == "__main__":
    host = "localhost:8080"
    endpoint = "/"
    duration = 10  # Dauer in Sekunden
    rate = measure_api_calls_per_second(host, endpoint, duration)
    print(f"API-Calls pro Sekunde (über {duration} Sekunden): {rate}")
