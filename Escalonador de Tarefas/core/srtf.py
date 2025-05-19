from core.base_scheduler import BaseScheduler
from copy import deepcopy

class SRTF(BaseScheduler):
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
                # Seleciona o processo com menor tempo restante
                ready.sort(key=lambda p: p.remaining_time)
                current = ready.pop(0)

                # Executa 1 unidade de tempo
                self.schedule.append(current.pid)
                current.remaining_time -= 1
                time += 1

                if current.remaining_time == 0:
                    current.end_time = time
                    current.turnaround_time = current.end_time - current.arrival_time
                    current.waiting_time = current.turnaround_time - current.duration
                    finished.append(current)
                    current = None
            else:
                time += 1
                current = None

        self.processes[:] = finished
