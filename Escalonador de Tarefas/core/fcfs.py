
from core.base_scheduler import BaseScheduler

class FCFS(BaseScheduler):
    def run(self):
        self.processes.sort(key=lambda p: p.arrival_time)
        time = 0
        for p in self.processes:
            if time < p.arrival_time:
                time = p.arrival_time
            p.start_time = time
            p.end_time = time + p.duration
            p.waiting_time = p.start_time - p.arrival_time
            p.turnaround_time = p.end_time - p.arrival_time
            time += p.duration
            self.schedule.append(p.pid)
