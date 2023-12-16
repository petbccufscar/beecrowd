while True:
    try:
        trace = input()
        trace_size = len(trace)
        total_proc = int(input())
        clocks = 0
        
        proc = total_proc
        for i, process in enumerate(trace):
            if process == 'R':
                #se nao atingiu o limite de processos
                #é possível ler outra vez no mesmo clock
                proc -=1
                #caso tenha chegado no fim do trace
                if i == trace_size - 1:
                    clocks += 1
                #caso tenha chegado no limite de processos
                #é necessário esperar o próximo clock
                elif proc == 0:               
                    clocks += 1
                    proc = total_proc    
            #caso process = W     
            else:
                #se estava lendo, é necessário esperar o próximo clock
                if proc != total_proc:
                    clocks += 1
                #contando o clock da escrita
                clocks += 1
                proc = total_proc
        print(clocks)    

    except EOFError:
        break 