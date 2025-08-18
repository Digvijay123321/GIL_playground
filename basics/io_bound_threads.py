import time, threading

JOBS = 50
SLEEP = 0.05  # simulate I/O wait

def io_job(i):
    time.sleep(SLEEP)  # releases GIL while sleeping
    return i

def run_serial():
    t0 = time.perf_counter()
    for i in range(JOBS):
        io_job(i)
    return time.perf_counter() - t0

def run_threads():
    t0 = time.perf_counter()
    threads = []
    for i in range(JOBS):
        t = threading.Thread(target=io_job, args=(i,))
        t.start(); threads.append(t)
    for t in threads: t.join()
    return time.perf_counter() - t0

if __name__ == "__main__":
    import time
    serial = run_serial()
    threaded = run_threads()
    print(f"Serial:   {serial:.3f}s")
    print(f"Threaded: {threaded:.3f}s  (expect much faster)")
