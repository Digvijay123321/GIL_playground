import math, time, threading

NUM_THREADS = 4
SIZE = 3_000_00

def cpu_heavy(n=SIZE):
    s = 0.0
    for i in range(n):
        s += math.sqrt(i % 1000)
    return s

def run_threads():
    threads = []
    results = [0.0] * NUM_THREADS

    def target(i):
        results[i] = cpu_heavy()

    t0 = time.perf_counter()
    for i in range(NUM_THREADS):
        t = threading.Thread(target=target, args=(i,))
        t.start(); threads.append(t)
    for t in threads: t.join()
    dt = time.perf_counter() - t0
    return sum(results), dt

def run_serial():
    t0 = time.perf_counter()
    total = sum(cpu_heavy() for _ in range(NUM_THREADS))
    dt = time.perf_counter() - t0
    return total, dt

if __name__ == "__main__":
    total_t, dt_t = run_threads()
    total_s, dt_s = run_serial()
    print(f"Serial:  {dt_s:.3f}s")
    print(f"Threads: {dt_t:.3f}s  (expect ~similar or slower)")
