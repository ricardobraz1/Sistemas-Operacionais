
from abc import ABC, abstractmethod

class BaseScheduler(ABC):
    def __init__(self, processes):
        self.processes = processes
        self.schedule = []

    @abstractmethod
    def run(self):
        pass

    def get_results(self):
        return self.schedule, self.processes
