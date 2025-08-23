import math, time, threading, multiprocessing as mp

WORKERS = 4
N = 1_200_000  # total work per worker

def cpu_heavy(n=N):
    s = 0.0
    for i in range(n):
        s += math.sqrt(i % 1000)
    return s

def threaded():
    results = [0.0] * WORKERS
    def target(i): results[i] = cpu_heavy()
    t0 = time.perf_counter()
    ts = [threading.Thread(target=target, args=(i,)) for i in range(WORKERS)]
    [t.start() for t in ts]; [t.join() for t in ts]
    return sum(results), time.perf_counter() - t0

def multiproc():
    t0 = time.perf_counter()
    with mp.Pool(WORKERS) as pool:
        res = pool.map(cpu_heavy, [N]*WORKERS)
    return sum(res), time.perf_counter() - t0

if __name__ == "__main__":
    _, t_thread = threaded()
    _, t_mp = multiproc()
    print(f"Threads:        {t_thread:.3f}s (GIL-constrained)")
    print(f"Multiprocessing:{t_mp:.3f}s (true parallelism)")
