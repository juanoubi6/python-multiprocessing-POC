from tasks import expensive_cpu_task, expensive_io_task


### Async pool map execution
# Expecting some of the expensive IO tasks to be executed while the expensive CPU task is being done
# to show that the main process is not waiting for all the pool tasks to finish to continue execution.
def execute_async_pool_tasks(process_pool):
    async_result = process_pool.map_async(expensive_io_task, range(10))
    print("Do an expensive CPU task to spend time")
    expensive_cpu_task(100)
    print("Finished executing an expensive CPU task")
    print("Do something meanwhile 2")
    print("Do something meanwhile 3")
    print("Do something meanwhile 4")
    print("Do something meanwhile 5")
    print("Do something meanwhile 6")
    print("Do something meanwhile 7")
    print("Do something meanwhile 8")
    print("Do something meanwhile 9")
    print("Do something meanwhile 10")
    async_result.wait()
    print("Waited until the pool finishes executing all tasks")
    print("Do something meanwhile 11")
    print("Do something meanwhile 12")
    print("Result: " + str(async_result.get()))
    process_pool.close()
