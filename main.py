#SSTF disk scheduling
def sstf_disk_scheduling(requests, initial_position):
    total_head_movement = 0
    current_position = initial_position

    while requests:
        nearest_request = min(requests, key=lambda x: abs(x - current_position))
        head_movement = abs(nearest_request - current_position)
        total_head_movement += head_movement
        current_position = nearest_request
        requests.remove(nearest_request)
    return total_head_movement

if __name__ == "__main__":
    disk_requests = [98, 183, 37, 122, 14, 124, 65, 67]
    initial_head_position = 53
    total_movement = sstf_disk_scheduling(disk_requests, initial_head_position)
    print("Total head movement using SSTF algorithm:", total_movement)



#FIFO page replacement algorithm
from queue import Queue

def pageFaults(pages, n, capacity):
    s = set()
    indexes = Queue()
    page_faults = 0
    for i in range(n):
        if (len(s) < capacity):
            if (pages[i] not in s):
                s.add(pages[i])
                page_faults = page_faults + 1
                indexes.put(pages[i])
        else:
            if (pages[i] not in s):
                val = indexes.queue[0]
                indexes.get()
                s.remove(val)
                s.add(pages[i])
                indexes.put(pages[i])
                page_faults += 1

    return page_faults

if __name__ == '__main__':
    pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    n = len(pages)
    capacity = 3
    print(pageFaults(pages, n, capacity))



#FCFS disk scheduling
def fcfs_disk_scheduling(requests, head):
    total_head_movements = 0
    sequence = []

    for request in requests:
        total_head_movements += abs(head - request)
        head = request
        sequence.append(request)

    return total_head_movements, sequence

if __name__ == "__main__":
    requests = [98, 183, 37, 122, 14, 124, 65, 67]
    initial_head_position = 53
    total_head_movements, sequence = fcfs_disk_scheduling(requests, initial_head_position)
    print("Total head movements:", total_head_movements)
    print("Sequence of disk accesses:", sequence)



#FCFS CPU scheduling
import pandas as pd

pid = ["p1", "p2", "p3", "p4", "p5"]
at = [0, 3, 4, 5, 5]
bt = [2, 4, 3, 3, 1]
n = len(pid)
for i in range(n):
    for j in range(0, n - i - 1):
        if at[j] > at[j + 1]:
            at[j], at[j + 1] = at[j + 1], at[j]
            pid[j], pid[j + 1] = pid[j + 1], pid[j]
            bt[j], bt[j + 1] = bt[j + 1], bt[j]
df = pd.DataFrame({"PID": pid, "AT": at, "BT": bt})
ct = []
tat = []
wt = []

for i in range(n):
    if i == 0:
        ct.append(at[0] + bt[0])
    else:
        ct.append(bt[i] + max(ct[i - 1], at[i]))

for i in range(n):
    tat.append(ct[i] - at[i])
    wt.append(tat[i] - bt[i])

df2 = pd.DataFrame({"PID": pid, "AT": at, "BT": bt, "CT": ct, "TAT": tat, "WT": wt})
avg_wt = sum(wt) / n
avg_tat = sum(tat) / n

print(df2)
print("Average Waiting Time:", avg_wt)
print("Average Turnaround Time:", avg_tat)



#LRU page replacement
capacity = 4
processList = [7, 0, 1, 2, 0, 3, 0,
               4, 2, 3, 0, 3, 2]

s = []
pageFaults = 0

for i in processList:
    if i not in s:
        if (len(s) == capacity):
            s.remove(s[0])
            s.append(i)
        else:
            s.append(i)
        pageFaults += 1

    else:
        s.remove(i)
        s.append(i)

print("{}".format(pageFaults))



#SJF CPU scheduling
def sstf_disk_scheduling(requests, initial_position):
    total_head_movement = 0
    current_position = initial_position

    while requests:
        nearest_request = min(requests, key=lambda x: abs(x - current_position))
        head_movement = abs(nearest_request - current_position)
        total_head_movement += head_movement
        current_position = nearest_request
        requests.remove(nearest_request)

    return total_head_movement

if __name__ == "__main__":
    disk_requests = [98, 183, 37, 122, 14, 124, 65, 67]
    initial_head_position = 53
    total_movement = sstf_disk_scheduling(disk_requests, initial_head_position)
    print("Total head movement using SSTF algorithm:", total_movement)



#producer consumer
import threading
import queue
import time

shared_queue = queue.Queue()
def producer():
    for i in range(10):
        data = f"Data {i}"
        print(f"Produced: {data}")
        shared_queue.put(data)
        time.sleep(1)

def consumer():
    while True:
        data = shared_queue.get()
        print(f"Consumed: {data}")
        time.sleep(2)
        shared_queue.task_done()

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)
producer_thread.start()
consumer_thread.start()
producer_thread.join()
shared_queue.join()
print("Program finished.")







