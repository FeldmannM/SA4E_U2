import http.client
import threading
import time
import random
import json

def make_get_request(host, endpoint):
    connection = http.client.HTTPConnection(host)
    connection.request("GET", endpoint)
    response = connection.getresponse()
    if response.status == 200:
        return True
    return False

def make_post_request(host, endpoint, data):
    headers = {'Content-type': 'application/json'}
    connection = http.client.HTTPConnection(host)
    connection.request("POST", endpoint, body=json.dumps(data), headers=headers)
    response = connection.getresponse()
    if response.status == 200:
        return True
    return False

def measure_api_calls_per_second(host, get_endpoint, post_endpoint, duration, post_data):
    start_time = time.time()
    count = 0
    lock = threading.Lock()

    def target():
        nonlocal count
        while time.time() - start_time < duration:
            if random.choice([True, False]):  # Zufällige Auswahl zwischen GET und POST
                if make_get_request(host, get_endpoint):
                    with lock:
                        count += 1
            else:
                if make_post_request(host, post_endpoint, post_data):
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
    host = "localhost:8080"
    get_endpoint = "/"  # Beispielendpunkt für GET-Anfragen
    post_endpoint = "/wishes"  # Beispielendpunkt für POST-Anfragen
    duration = 10  # Dauer in Sekunden

    # Beispiel-Daten für POST-Anfragen
    post_data = {"key": "value"}

    combined_rate = measure_api_calls_per_second(host, get_endpoint, post_endpoint, duration, post_data)
    print(f"Kombinierte API-Calls pro Sekunde (über {duration} Sekunden): {combined_rate}")
