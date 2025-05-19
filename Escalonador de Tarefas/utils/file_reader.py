
from models.process import Process

def read_processes_from_file(filename):
    processes = []
    with open(filename, 'r') as f:
        for line in f:
            if line.strip() == '' or line.startswith('#'):
                continue
            parts = line.strip().split()
            if len(parts) == 5:
                pid, arrival, duration, priority, ptype = parts
                processes.append(Process(pid, int(arrival), int(duration), int(priority), int(ptype)))
    return processes
