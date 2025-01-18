import http.client
import threading
import time

def make_request(host, endpoint):
    connection = http.client.HTTPConnection(host)
    connection.request("GET", endpoint)
    response = connection.getresponse()
    if response.status == 200:
        return True
    return False

def measure_api_calls_per_second(host, endpoint, duration):
    start_time = time.time()
    count = 0
    lock = threading.Lock()

    def target():
        nonlocal count
        while time.time() - start_time < duration:
            if make_request(host, endpoint):
                with lock:
                    count += 1

    threads = []
    for _ in range(10):  # Die Anzahl der Threads kann angepasst werden
        thread = threading.Thread(target=target)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    elapsed_time = time.time() - start_time
    return count / elapsed_time

if __name__ == "__main__":
    host = "localhost:5000"
    endpoint = "/wishes"
    duration = 10  # Dauer in Sekunden
    rate = measure_api_calls_per_second(host, endpoint, duration)
    print(f"API-Calls pro Sekunde (über {duration} Sekunden): {rate}")