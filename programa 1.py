import random

class cpu:
    fila=[]
    
    def adicionarProcesso(self,processo):
        self.fila.append(processo)

class proc:
    def __init__(self,nome):
        self.id=random.randint(1,60)
        self.nome=f"{nome}"
    

celeron=cpu()
celeron.adicionarProcesso("hello")
print(celeron.fila)

vscode=proc("VS Code")
celeron.adicionarProcesso(vscode)
print(celeron.fila[1].id)