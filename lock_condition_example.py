import threading
import time

buffer = []
MAX_ITEMS = 10

lock = threading.Lock()
condition = threading.Condition(lock)

def producer():
    global buffer
    while True:
        with condition:
            if len(buffer) < MAX_ITEMS:
                item = "item"
                buffer.append(item)
                print(f"Wyprodukowano {item}. Rozmiar bufora: {len(buffer)}")
                condition.notify()
            condition.wait_for(lambda: len(buffer) < MAX_ITEMS)
            time.sleep(1)
def consumer():
    global buffer
    while True:
        with condition:
            if buffer:
                item = buffer.pop(0)
                print(f"Zużyto {item}. Rozmiar bufora: {len(buffer)}")
                condition.notify()
            condition.wait_for(lambda: buffer)
            time.sleep(1)

producer_threads = [threading.Thread(target=producer) for _ in range(2)]
consumer_threads = [threading.Thread(target=consumer) for _ in range(2)]

for thread in producer_threads + consumer_threads:
    thread.start()

for thread in producer_threads + consumer_threads:
    thread.join()

print(f"Końcowa wartość współdzielonego zasobu: {len(buffer)}")
