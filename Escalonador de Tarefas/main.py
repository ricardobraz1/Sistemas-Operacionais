from utils.file_reader import read_processes_from_file
from utils.results import print_results
from core.fcfs import FCFS
from core.sjf import SJF
from core.rr import RoundRobin
from core.srtf import SRTF
from core.prioc import Prioc
from core.priop import Priop

# Define os algoritmos disponíveis por tipo de processo
algoritmos_por_tipo = {
    1: [FCFS, SJF],
    2: [SRTF, Prioc],
    3: [Priop, RoundRobin]
}

def main():
    filename = input("Digite o nome do arquivo .txt com os processos (ex: FCFS_SJF_6.txt): ").strip()
    processos = read_processes_from_file(filename)

    tipos = {1: [], 2: [], 3: []}
    for p in processos:
        tipos[p.ptype].append(p)

    for tipo, lista in tipos.items():
        if not lista:
            continue
        print(f"\n--- Tipo de processo: {tipo} ---")
        algs = algoritmos_por_tipo[tipo]
        print(f"[1] {algs[0].__name__}  |  [2] {algs[1].__name__}")
        escolha = input("Escolha o algoritmo (1 ou 2): ").strip()

        # Resetar os processos antes de executar
        for p in lista:
            p.reset()

        algo_escolhido = algs[int(escolha) - 1].__name__

        if algo_escolhido in ["RoundRobin", "Priop", "SRTF"]:
            print("Quantum padrão = 1")
            novo_quantum = input("Deseja alterar o quantum? (pressione Enter para manter): ").strip()
            quantum = int(novo_quantum) if novo_quantum else 1
            escalonador = algs[int(escolha) - 1](lista, quantum=quantum)
        else:
            escalonador = algs[int(escolha) - 1](lista)

        escalonador.run()
        schedule, finalizados = escalonador.get_results()
        print_results(schedule, finalizados)

if __name__ == "__main__":
    main()
