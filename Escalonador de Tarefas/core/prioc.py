
from core.base_scheduler import BaseScheduler
from copy import deepcopy

class Prioc(BaseScheduler):
    def run(self):
        queue = sorted(deepcopy(self.processes), key=lambda p: (p.arrival_time, -p.priority))
        ready = []
        time = 0
        finished = []
        while queue or ready:
            while queue and queue[0].arrival_time <= time:
                ready.append(queue.pop(0))
            if not ready:
                time += 1
                continue
            ready.sort(key=lambda p: -p.priority)
            current = ready.pop(0)
            current.start_time = time
            current.end_time = time + current.duration
            current.waiting_time = current.start_time - current.arrival_time
            current.turnaround_time = current.end_time - current.arrival_time
            time += current.duration
            self.schedule.append(current.pid)
            finished.append(current)
        self.processes[:] = finished
