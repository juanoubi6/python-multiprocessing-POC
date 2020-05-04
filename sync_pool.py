from tasks import expensive_io_task


### Sync pool map execution
# The pool distributes the tasks to the available processors using a FIFO scheduling.
# Expecting the main process to stop until all the pool tasks are completed.
def execute_sync_pool_tasks(process_pool):
    sync_result = process_pool.map(expensive_io_task, range(10))
    print("Result: " + str(sync_result))
    print("All pool tasks finished, resume execution of main process")
    print("Do something 1")
    print("Do something 2")
    process_pool.close()
