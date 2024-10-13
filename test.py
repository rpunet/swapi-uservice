import requests
import threading

url = 'http://100.77.107.161:30007/people'

def send_request():
    response = requests.get(url)

def test_traffic_load(concurrent_requests):
    threads = []

    for _ in range(concurrent_requests):
        thread = threading.Thread(target=send_request)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

test_traffic_load(10)
