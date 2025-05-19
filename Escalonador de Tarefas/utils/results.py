
def print_results(schedule, processes):
    print("Ordem de execução (PID):", schedule)
    total_waiting = sum(p.waiting_time for p in processes)
    total_turnaround = sum(p.turnaround_time for p in processes)
    n = len(processes)
    print(f"Tempo médio de espera: {total_waiting / n:.2f}")
    print(f"Tempo médio de execução: {total_turnaround / n:.2f}")
