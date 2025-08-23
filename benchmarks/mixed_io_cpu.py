import time, math, threading

THREADS = 8

def io_then_cpu(i):
    # I/O part (releases GIL)
    time.sleep(0.05)
    # CPU part (contends on GIL)
    s = 0.0
    for k in range(200_000):
        s += math.sqrt((k + i) % 1000)
    return s

def main():
    t0 = time.perf_counter()
    ts = []
    def target(): io_then_cpu(0)
    for _ in range(THREADS):
        t = threading.Thread(target=target)
        t.start(); ts.append(t)
    for t in ts: t.join()
    print(f"Total time: {time.perf_counter() - t0:.3f}s")

if __name__ == "__main__":
    main()
