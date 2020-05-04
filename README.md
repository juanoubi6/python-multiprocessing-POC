Using the multiprocessing library to parallelize the execution of many tasks.

https://www.ellicium.com/python-multiprocessing-pool-process/

How to run it
```sh
python3 main.py <execution_mode>
```

Available execution modes to test
  - sync-pool: executes a series of tasks using the multiprocessing library Pool's **map** function.
  - async-pool: executes a series of tasks using the multiprocessing library Pool's **map_async** function.
  - sync-process-with-io-tasks: execute IO tasks using independent processes with Process class.
  - sync-process-with-cpu-tasks: execute CPU tasks using independent processes with Process class.
  
