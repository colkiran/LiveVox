
import threading
import time


def doJob(secs, tname):
    print(f"Going to sleep for 2 secs......{tname}")
    time.sleep(secs)
    print(f"Just got up from sleep........{tname}")

ST = time.perf_counter()

threads = []

for i in range(50):
    t = threading.Thread(target=doJob, name = "th" + str(i), args = (2, "th" + str(i)))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

ET = time.perf_counter()
print(f"The total time taken by the task is {ET - ST}")