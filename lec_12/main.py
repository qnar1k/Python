import random
import time

def generate_file(file_name, lines=100, numbers_per_line=20):
    with open(file_name, "w") as file:
        for _ in range(lines):
            random_numbers = " ".join(str(random.randint(1, 100)) for _ in range(numbers_per_line))
            file.write(random_numbers + "\n")
    print(f"File '{file_name}' generated with {lines} lines of random numbers.")

def read_and_process_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    return [list(map(int, line.split())) for line in lines]

def filter_numbers(data):
    return [[num for num in row if num > 40] for row in data]

def write_file(file_name, data):
    with open(file_name, "w") as file:
        for row in data:
            file.write(" ".join(map(str, row)) + "\n")
    print(f"Filtered data written back to '{file_name}'.")

def read_file_generator(file_name):
    with open(file_name, "r") as file:
        for line in file:
            yield list(map(int, line.split()))

def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time for {func.__name__}: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@execution_time
def main():
    file_name = "random_numbers.txt"
    
    generate_file(file_name)
    
    data = read_and_process_file(file_name)
    
    filtered_data = filter_numbers(data)
    
    write_file(file_name, filtered_data)
    
    print("\nReading filtered file as generator:")
    for row in read_file_generator(file_name):
        print(row)  

if __name__ == "__main__":
    main()
