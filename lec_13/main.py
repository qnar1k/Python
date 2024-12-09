import time
import threading
import multiprocessing
from collections import Counter

def generate_large_file(filename, num_lines=1000000):
    import random
    import string
    with open(filename, 'w') as f:
        for _ in range(num_lines):
            line = ' '.join(''.join(random.choices(string.ascii_lowercase, k=5)) for _ in range(10))
            f.write(line + '\n')

def count_words_sequential(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
    return Counter(words)

def count_words_chunk(chunk):
    return Counter(chunk.split())

def count_words_multithreading(filename, num_threads=4):
    with open(filename, 'r') as file:
        content = file.read()
    chunk_size = len(content) // num_threads
    threads = []
    counters = []
    for i in range(num_threads):
        start = i * chunk_size
        end = None if i == num_threads - 1 else (i + 1) * chunk_size
        chunk = content[start:end]
        counter = Counter()
        thread = threading.Thread(target=lambda c: c.update(count_words_chunk(chunk)), args=(counter,))
        threads.append(thread)
        counters.append(counter)
        thread.start()
    for thread in threads:
        thread.join()
    return sum(counters, Counter())

def count_words_multiprocessing(filename, num_processes=4):
    with open(filename, 'r') as file:
        content = file.read()
    chunk_size = len(content) // num_processes
    chunks = [content[i * chunk_size: None if i == num_processes - 1 else (i + 1) * chunk_size] for i in range(num_processes)]
    with multiprocessing.Pool(processes=num_processes) as pool:
        counters = pool.map(count_words_chunk, chunks)
    return sum(counters, Counter())

if __name__ == "__main__":
    filename = "large_text.txt"
    generate_large_file(filename)

    start = time.time()
    sequential_result = count_words_sequential(filename)
    sequential_time = time.time() - start

    start = time.time()
    multithreading_result = count_words_multithreading(filename)
    multithreading_time = time.time() - start

    start = time.time()
    multiprocessing_result = count_words_multiprocessing(filename)
    multiprocessing_time = time.time() - start

    print(f"Sequential Time: {sequential_time:.2f}s")
    print(f"Multithreading Time: {multithreading_time:.2f}s")
    print(f"Multiprocessing Time: {multiprocessing_time:.2f}s")
    print(f"Speedup (Multithreading): {sequential_time / multithreading_time:.2f}x")
    print(f"Speedup (Multiprocessing): {sequential_time / multiprocessing_time:.2f}x")
