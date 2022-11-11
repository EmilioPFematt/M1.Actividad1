from act_1_cleaningmodel.cleaning_model import CleaningModel
import time

def cleaning_space(num_agents, width, height, percent, limitTime):
    model = CleaningModel(num_agents, width, height, percent)
    suc_ini = len(model.dirty_Matrix)
    init_time = int(time.time() * 1000)
    cur_time = init_time
    while(len(model.dirty_Matrix) > 0) and (cur_time - init_time < limitTime * 1000):
        model.step()
        cur_time = int(time.time() * 1000)
    suc_fin = len(model.dirty_Matrix)
    
    print("Numero de Agentes:", num_agents)
    print("Dimensiones de la matriz:", width, "*", height)
    print("Porcentaje inicial de celdas sucias:", percent*100)
    print("Limite de tiempo en segundos:", limitTime)
    if(cur_time-init_time >= limitTime*1000):
        print("LLEGO AL TIEMPO LIMITE")
    print("Porcentaje de celdas limpias: ", ((width*height)-suc_fin)/(width*height)*100)
    print("Movimientos realizados por agente: ")
    for i in model.schedule.agents :
        print("Agente ", i.unique_id, i.counter, "movimientos")

#Numero de agentes, width, height, porcentaje de celdas sucias, tiempo de ejecucion(s)
cleaning_space(15, 70, 70, 0.5, 0.35) 