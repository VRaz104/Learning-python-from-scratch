#A problem using context managers:
#Create a context manager that :
    #Prints "== Starting ==" before the with block runs
    #Prints "== Ending ==" after the block finishes
    #how long the block took to execute
    #Prints the elapsed time at the end of the block

import time
class demo:
    def __enter__(self):
        print("== Starting ==")
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print("== Ending == ")
        self.end = time.perf_counter()
        elapsed_time = self.end-self.start
        print(f"This code code took {elapsed_time} seconds to run")       
with demo() as msg:
    print(msg)