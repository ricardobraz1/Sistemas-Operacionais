from core.base_scheduler import BaseScheduler
from copy import deepcopy

class RoundRobin(BaseScheduler):
    def __init__(self, processes, quantum=1):
        super().__init__(processes)
        self.quantum = quantum

    def run(self):
        queue = sorted(deepcopy(self.processes), key=lambda p: p.arrival_time)
        ready = []
        time = 0
        finished = []
        while queue or ready:
            while queue and queue[0].arrival_time <= time:
                ready.append(queue.pop(0))
            if not ready:
                time += 1
                continue
            current = ready.pop(0)
            exec_time = min(self.quantum, current.remaining_time)
            time += exec_time
            current.remaining_time -= exec_time
            self.schedule.extend([current.pid] * exec_time)
            while queue and queue[0].arrival_time <= time:
                ready.append(queue.pop(0))
            if current.remaining_time > 0:
                ready.append(current)
            else:
                current.end_time = time
                current.turnaround_time = current.end_time - current.arrival_time
                current.waiting_time = current.turnaround_time - current.duration
                finished.append(current)
        self.processes[:] = finished
