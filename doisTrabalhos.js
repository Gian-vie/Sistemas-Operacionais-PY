export class Cpu {
    
    constructor(){
        this.quantum = 5;
        this.tempoExecucao = 0;
        this.fila = []
    }

    adicionarProcesso(processo){
        this.fila.push(processo)
        console.log(this.fila)
    }

    executarProcessos(){
        while (this.fila.length > 0) {
            let process = this.fila[0]
            if(process.quantum <= this.quantum){
                this.tempoExecucao += process.quantum
                
            }
        }
    }

}

let cpuz = new Cpu

cpuz.adicionarProcesso("pss1")
cpuz.adicionarProcesso("pss2")
cpuz.adicionarProcesso("pss3")