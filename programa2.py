import tkinter as tk
import random

class Proc:
    def __init__(self, nome):
        self.nome = str(nome)
        self.tempo = random.randint(5, 200)

class CPU:
    def __init__(self):
        self.fila = []
        self.quantum = 5
        self.tempoExec = 0

    def adicionarProcesso(self, processo):
        self.fila.append(processo)

    def executar1Tick(self):
        if len(self.fila) == 0:
            return "Sem processos"

        atual = self.fila[0]
        if atual.tempo <= self.quantum:
            self.tempoExec += atual.tempo
            self.fila.pop(0)
            return f"{atual.nome} finalizado!"
        else:
            atual.tempo -= self.quantum
            self.tempoExec += self.quantum
            self.fila.append(self.fila.pop(0))
            return f"{atual.nome} executado por {self.quantum}, resta {atual.tempo}"

    def situacaoAtual(self):
        return self.fila[0] if self.fila else None

class SimuladorInterface:
    def __init__(self, master):
        self.cpu = CPU()
        self.master = master
        master.title("Simulador de CPU")
        master.configure(bg='#1e1e1e')
        master.geometry("750x300")

        self.contador_nome = 1

        # Estilo
        self.fonte = ("Courier New", 11)
        self.cor_fg = "#eeeeee"
        self.bg = "#1e1e1e"
        self.highlight = "#444444"

        # ====== Painéis ======
        self.left_frame = tk.Frame(master, bg=self.bg)
        self.left_frame.pack(side="left", fill="y", padx=20, pady=20)

        self.center_frame = tk.Frame(master, bg=self.bg)
        self.center_frame.pack(side="left", fill="both", expand=True, padx=20)

        self.right_frame = tk.Frame(master, bg=self.bg)
        self.right_frame.pack(side="right", fill="y", padx=20, pady=20)

        # ====== Lado Esquerdo ======
        self.lbl_num_proc = tk.Label(self.left_frame, text="Processos: 00", fg=self.cor_fg, bg=self.bg, font=self.fonte)
        self.lbl_num_proc.pack(pady=10)

        self.btn_add_proc = tk.Button(self.left_frame, text="Adicionar Processo", command=self.adicionar_processo,
                                      font=self.fonte, bg=self.highlight, fg=self.cor_fg)
        self.btn_add_proc.pack(pady=10)

        # Área de console
        self.console_frame = tk.LabelFrame(master, text="Console", fg="white", bg="black", bd=2, relief="groove", font=("Courier", 10))
        self.console_frame.place(x=20, y=120, width=200, height=150)
        
        self.console_text = tk.Text(self.console_frame, bg="black", fg="white", font=("Courier", 9), wrap="word")
        self.console_text.pack(expand=True, fill="both")


        # ====== Centro (CPU) ======
        self.cpu_frame = tk.LabelFrame(master, text="CPU", fg="white", bg="black", font=("Courier", 12), bd=2, relief="groove")
        self.cpu_frame.place(x=250, y=20, width=220, height=160)

        self.lbl_quantum = tk.Label(self.cpu_frame, text="Quantum : 05", fg="white", bg="black", anchor="w")
        self.lbl_quantum.pack(anchor="w", padx=10)

        self.lbl_tempo_exec = tk.Label(self.cpu_frame, text="Tempo de execução : 000", fg="white", bg="black", anchor="w")
        self.lbl_tempo_exec.pack(anchor="w", padx=10)

        self.lbl_proc_restante = tk.Label(self.cpu_frame, text="Tempo restante : --", fg="white", bg="black", anchor="w")
        self.lbl_proc_restante.pack(anchor="w", padx=10)

        self.lbl_nome_proc = tk.Label(self.cpu_frame, text="Processo: N/A", fg="white", bg="black", anchor="w")
        self.lbl_nome_proc.pack(anchor="w", padx=10)


        # ====== Lado Direito ======
        self.btn_tick = tk.Button(self.right_frame, text="⏱ Passar 1 Tempo", command=self.executar_tick,
                                  font=self.fonte, bg=self.highlight, fg=self.cor_fg)
        self.btn_tick.pack(pady=5, fill="x")

        self.btn_exec_all = tk.Button(self.right_frame, text="▶ Executar Tudo", command=self.executar_tudo,
                                      font=self.fonte, bg=self.highlight, fg=self.cor_fg)
        self.btn_exec_all.pack(pady=5, fill="x")

        self.lbl_set_q = tk.Label(self.right_frame, text="Quantum:", fg=self.cor_fg, bg=self.bg, font=self.fonte)
        self.lbl_set_q.pack(pady=(15, 2))

        self.entry_quantum = tk.Entry(self.right_frame, width=5, font=self.fonte, bg="#2e2e2e", fg=self.cor_fg,
                                      insertbackground=self.cor_fg, justify="center")
        self.entry_quantum.insert(0, "05")
        self.entry_quantum.pack(pady=2)

        self.btn_set_quantum = tk.Button(self.right_frame, text="Definir", command=self.definir_quantum,
                                         font=self.fonte, bg=self.highlight, fg=self.cor_fg)
        self.btn_set_quantum.pack(pady=5)

        # Atualizar exibição inicial
        self.atualizar_interface()

    def adicionar_processo(self):
        nome = f"P{self.contador_nome}"
        self.contador_nome += 1
        processo = Proc(nome)
        self.cpu.adicionarProcesso(processo)
        self.atualizar_interface()

    def executar_tick(self):
        resultado = self.cpu.executar1Tick()
        self.log_console(resultado)
        self.atualizar_interface()

    def log_console(self, texto):
        self.console_text.insert(tk.END, texto + "\n")
        self.console_text.see(tk.END)

    def executar_tudo(self):
        while self.cpu.fila:
            self.executar_tick()
            self.master.update()  # Atualiza a interface visual


    def definir_quantum(self):
        try:
            valor = int(self.entry_quantum.get())
            self.cpu.quantum = valor
            self.lbl_quantum.config(text=f"Quantum : {valor:02d}")
        except ValueError:
            pass

    def atualizar_interface(self):
        self.lbl_num_proc.config(text=f"Processos: {len(self.cpu.fila):02d}")
        self.lbl_tempo_exec.config(text=f"Tempo de execução : {self.cpu.tempoExec:03d}")
        proc = self.cpu.situacaoAtual()
        if proc:
            self.lbl_nome_proc.config(text=f"Processo: {proc.nome}")
            self.lbl_proc_restante.config(text=f"Tempo restante : {proc.tempo:02d}")
        else:
            self.lbl_nome_proc.config(text="Processo: N/A")
            self.lbl_proc_restante.config(text="Tempo restante : --")


# Executar
root = tk.Tk()
app = SimuladorInterface(root)
root.mainloop()
