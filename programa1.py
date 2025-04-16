import random

class cpu:
    def __init__(self):
        self.fila=[]
        self.quantum=5
        self.tempoExec=0
    
    def adicionarProcesso(self,processo):
        self.fila.append(processo)
        print(f"Processo {processo.nome}, tempo {processo.tempo} adicionado")
    
    def executarProcessos(self):
        while len(self.fila)>0:
            if(self.fila[0].tempo<=self.quantum): # verifica se o processo é pequeno e será eliminado
                self.tempoExec+=self.fila[0].tempo
                temp=""
                for x in range(1,len(self.fila)):
                    temp+=" "+self.fila[x].nome
                if temp=="": temp=" nenhum processo"
                print(f"{self.fila[0].nome} eliminado, restam:{temp}")
                self.fila.pop(0)
            else: # quando o processo é grande e ainda não será eliminado
                self.fila[0].tempo-=self.quantum
                self.tempoExec+=self.quantum
                print(f"{self.fila[0].nome} resta {self.fila[0].tempo} de tempo")
                self.fila.append(self.fila[0])
                self.fila.pop(0)
    
    def situacaoAtual(self):
        if(len(self.fila)>0):
            string=f"{len(self.fila)} processos abertos, quantum={self.quantum}\n"
            for item in self.fila:
                string+=f"\nProcesso {item.nome}\nTempo: {item.tempo}\n"
            return string
        else:
            string=f"Sem processos pendentes, quantum={self.quantum}"
            return string

class proc:
    def __init__(self,nome):
        self.nome=str(nome)
        self.tempo=random.randint(5,200)

celeron=cpu()
celeron.adicionarProcesso(proc("OBS"))
celeron.adicionarProcesso(proc("Calculadora"))
celeron.adicionarProcesso(proc("Excel"))
celeron.adicionarProcesso(proc("Gerenciador de Tarefas"))
# print(celeron.situacaoAtual())
celeron.executarProcessos()
# print(celeron.situacaoAtual())