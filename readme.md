# Simulador de Escalonamento de Processos Round-Robin

Este projeto é um simulador gráfico de uma CPU que utiliza o algoritmo **Round-Robin** para escalonamento de processos. Desenvolvido em **Python**. A interface foi construída em **Tkinter**, o qual permite adicionar processos, configurar quantum e visualizar a execução passo a passo.

## Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-lightgrey)
![Sistema Operacional](https://img.shields.io/badge/Linux-suportado-green)

---

## Funcionalidades

- Adição de processos com tempo de execução aleatório (entre 5 e 200 unidades).
- Execução de um único "tick" de CPU com base no quantum configurado.
- Execução contínua até esvaziar a fila de processos.
- Definição dinâmica do valor de quantum.
- Interface gráfica com painel de status e console para acompanhar a execução.

---

## Como Funciona o Algoritmo Round-Robin

O algoritmo **Round-Robin** funciona por meio de uma fila circular. Cada processo recebe uma fatia de tempo (quantum) para executar. Se ele terminar dentro desse tempo, é removido da fila. Caso contrário, seu tempo restante é decrementado, e ele volta para o fim da fila. Isso garante um escalonamento justo, impedindo que um único processo monopolize a CPU.

### Ciclo de execução:

1. Seleciona o primeiro processo da fila.
2. Se o tempo restante for menor ou igual ao quantum:
   - Executa o processo completamente e o remove da fila.
3. Caso contrário:
   - Executa por um quantum, atualiza o tempo restante e o move para o final da fila.
4. O tempo total de execução da CPU é incrementado conforme os ticks.

---

## Estrutura do Projeto

- `Proc`: Classe que representa um processo, com tempo de execução aleatório.
- `CPU`: Simula o comportamento da CPU com fila, quantum e execução por tick.
- `SimuladorInterface`: Interface gráfica com botões de controle e painel de status.

---

## Instalação e Execução (Linux)

Siga os passos abaixo para rodar o projeto em uma máquina Linux com Python instalado.

### 1. Atualize os pacotes do sistema

```bash
sudo apt update
sudo apt upgrade
```

### 2. Instale o python e a biblioteca Tkinter
```bash
sudo apt install python3 python3-tk
```

### 3. Clone o repositório
```bash
git clone https://github.com/Gian-vie/Sistemas-Operacionais-PY.git
```

### 4. Execute o simulador

```bash
python3 simulador.py
```

---

## Autores

- [Cristian Doring Molon](https://github.com/cristiandoring)
- [Diego Vinicius Gonçalves](https://github.com/unknooly)
- [Gian Carlos Vieceli](https://github.com/Gian-vie)

