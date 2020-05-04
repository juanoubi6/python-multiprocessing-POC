from multiprocessing import cpu_count, Pool
import sys
import async_pool
import sync_pool
import sync_process
import time

if __name__ == '__main__':
    execution_mode = sys.argv[1]

    # Get CPU amount
    cpu_number = cpu_count()
    print("Number of CPUs: " + str(cpu_number))

    # Create pool of processes
    process_pool = Pool(cpu_number)

    start = time.time()
    if execution_mode == "async-pool":
        async_pool.execute_async_pool_tasks(process_pool)
    elif execution_mode == "sync-pool":
        sync_pool.execute_sync_pool_tasks(process_pool)
    elif execution_mode == 'sync-process-with-io-tasks':
        sync_process.execute_io_tasks_with_processes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    elif execution_mode == 'sync-process-with-cpu-tasks':
        sync_process.execute_cpu_tasks_with_processes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    else:
        print("Invalid execution mode")

    end = time.time()
    print("Time elapsed in seconds: {}".format(end-start))