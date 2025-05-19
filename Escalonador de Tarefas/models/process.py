
class Process:
    def __init__(self, pid, arrival_time, duration, priority, ptype):
        self.pid = pid
        self.arrival_time = arrival_time
        self.duration = duration
        self.remaining_time = duration
        self.priority = priority
        self.ptype = ptype
        self.start_time = None
        self.end_time = None
        self.waiting_time = 0
        self.turnaround_time = 0

    def reset(self):
        self.remaining_time = self.duration
        self.start_time = None
        self.end_time = None
        self.waiting_time = 0
        self.turnaround_time = 0
