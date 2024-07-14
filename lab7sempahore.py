import threading
import time

shared_resource = 0
semaphore = threading.Semaphore(1)

def access_resource():
    global shared_resource
    print(f"{threading.current_thread().name} próbuje uzyskać dostęp do udostępnionego zasobu na komputerze numeru indeksu 67240")
    semaphore.acquire()
    print(f"{threading.current_thread().name} uzyskała dostęp do zasobu współdzielonego na komputerze numeru indeksu 67240.")
    local_copy = shared_resource
    local_copy += 1
    time.sleep(1)
    shared_resource = local_copy
    print(f"{threading.current_thread().name} zwalnia zasób współdzielony na komputerze numeru indeksu 67240.")
    semaphore.release()

threads = []
for i in range(5):
    thread = threading.Thread(target=access_resource)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(f"Końcowa wartość współdzielonego zasobu: {shared_resource}")
