import random

class cpu:
    def __init__(self):
        self.fila=[]
        self.quantum=5
        self.tempoExec=0
        self.status="on"
    
    def adicionarProcesso(self,processo):
        self.fila.append(processo)
        self.status="off"
    
    def desligar(self):
        print(f"Tempo total de execução: {self.tempoExec}")
    
    def executarProcesso(self,processo):
        if(self.status=="off"): return # se PC desligado, não pode executar processos
        
        if(len(self.fila)>0): # len(fila) = tamanho da fila => se não tem processo, então termina execuções
            if(self.fila[0].tempo<=self.quantum): # verifica se o processo é pequeno e será eliminado
                self.tempoExec+=self.fila[0].tempo
                # inserir código pra eleminar o processo
            else: # quando o processo é grande e ainda não será eliminado
                self.fila[0].tempo-=self.quantum
                self.tempoExec+=self.quantum
                # inserir código pra retirar o processo da primeira posição da fila
                self.fila.append(processo)
        else:
            self.desligar() # sem processos, então desligar o PC
    
    def situacaoAtual(self):
        string=f"Processador {self.status.upper()} com {len(self.fila)} processos abertos, quantum={self.quantum}"
        for item in self.fila:
            string+=f"\n\nProcesso {item.nome}\nTempo: {item.tempExec}"
        return string+"\n"

class proc:
    def __init__(self,nome):
        self.nome=str(nome)
        self.tempExec=random.randint(1,200)
    

celeron=cpu()
vscode=proc("VS Code")
chrome=proc("Chrome")
print(celeron.situacaoAtual())
celeron.adicionarProcesso(vscode)
celeron.adicionarProcesso(chrome)
print(celeron.situacaoAtual())
celeron.executarProcesso(vscode)
