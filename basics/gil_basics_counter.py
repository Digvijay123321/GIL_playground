import threading

N = 5_000_00  # 500k increments per thread
NUM_THREADS = 4

counter = 0
lock = threading.Lock()

def work():
    global counter
    for _ in range(N):
        with lock:
            counter += 1

def main():
    threads = [threading.Thread(target=work) for _ in range(NUM_THREADS)]
    for t in threads: t.start()
    for t in threads: t.join()

    expected = N * NUM_THREADS
    print(f"Counter={counter:,}, Expected={expected:,}, Match={counter == expected}")

if __name__ == "__main__":
    main()
