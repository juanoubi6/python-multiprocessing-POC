from multiprocessing import Process
from tasks import expensive_io_task, expensive_cpu_task


### Process execution
# Launch one process per task. The process class puts all the processes in memory and schedules
# execution using FIFO policy. When the process is suspended, it pre-empts and schedules new process
# for execution.
def execute_io_tasks_with_processes(tasks_data):
    execute_task_with_process(expensive_io_task, tasks_data)


def execute_cpu_tasks_with_processes(tasks_data):
    execute_task_with_process(expensive_cpu_task, tasks_data)


def execute_task_with_process(task, tasks_data):
    process_list = []
    for data in tasks_data:
        process = Process(target=task, args=(data,))
        process_list.append(process)
        process.start()

    for process in process_list:
        process.join()
