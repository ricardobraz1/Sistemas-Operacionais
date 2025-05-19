from core.base_scheduler import BaseScheduler
from copy import deepcopy

class Priop(BaseScheduler):
    def __init__(self, processes, quantum=1):
        super().__init__(processes)
        self.quantum = quantum

    def run(self):
        queue = sorted(deepcopy(self.processes), key=lambda p: p.arrival_time)
        ready = []
        time = 0
        finished = []
        current = None
        while queue or ready or current:
            while queue and queue[0].arrival_time <= time:
                ready.append(queue.pop(0))
            if current:
                ready.append(current)
            if ready:
                ready.sort(key=lambda p: -p.priority)
                current = ready.pop(0)
                exec_time = min(self.quantum, current.remaining_time)
                for _ in range(exec_time):
                    self.schedule.append(current.pid)
                    current.remaining_time -= 1
                    time += 1
                    if current.remaining_time == 0:
                        break
                if current.remaining_time == 0:
                    current.end_time = time
                    current.turnaround_time = current.end_time - current.arrival_time
                    current.waiting_time = current.turnaround_time - current.duration
                    finished.append(current)
                    current = None
                else:
                    ready.append(current)
                    current = None
            else:
                time += 1
        self.processes[:] = finished
