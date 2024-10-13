import requests
import threading
import time

url = 'http://100.77.107.161:30007/people'   #use minikube ip

def send_request():
    response = requests.get(url)
    if response.status_code != 200:
        print("Request failed")
    else:
        print(f"Response code: {response.status_code} OK")

def test_traffic_load(concurrent_requests, duration):
    threads = []
    initial_time = time.time()

    while time.time() - initial_time < duration:
        for _ in range(concurrent_requests):
            thread = threading.Thread(target=send_request)
            thread.start()
            threads.append(thread)

        time.sleep(1)

    for thread in threads:
        thread.join()

test_traffic_load(10, 60)  # args: concurrent requests, duration time
