import time

def cpu_intensive_task():
    # Example of a CPU-intensive task: calculating a list of squared integers
    data = [i*i for i in range(100000000)]

def main():
    # Record start time
    time_start = time.perf_counter()
    
    # Execute the CPU-intensive task
    cpu_intensive_task()
    
    # Record end time
    time_end = time.perf_counter()
    
    # Calculate the duration
    time_duration = time_end - time_start
    
    # Report the duration
    print(f'Took {time_duration:.3f} seconds')

if __name__ == '__main__':
    main()