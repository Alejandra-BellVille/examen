#class Tarea:   
def __init__(self, descripcion, fecha_limite): 
       self.descripcion = descripcion        
       self.fecha_limite = fecha_limite       
       self.__estado = "pendiente"        
       self.__id_tarea = 1    
        
       def marcar_completada(self):        
           self.__estado = "completada"        
           print(f"Tarea '{self.descripcion}' marcada como completada.")    
           def esta_pendiente(self): 
               
def obtener_id(self):
       return self.__estado == "pendiente"    def __str__(self): 
def __str__(self):
       return f"Tarea: {self.descripcion} (Fecha Límite: {self.fecha_limite}, Estado: {self.estado})"  


#class GestorTareas:

def __init__(self):
        
        self.tareas = []

def agregar_tarea(self, tarea):
        
        # b)	Implemente el método agregar_tarea(self, tarea) que reciba un objeto Tarea y lo añada a la lista interna del gestor. 
        
        self.tareas.append(tarea) #agregue tarea

def listar_todas_tareas(self):
        # c) Implemente el método listar_todas_tareas(self) que imprima la descripción y el estado de todas las tareas. 
        if not self.tareas: #verifica si la lista esta vacia
        print("No hay tareas en el gestor")
        return
        for tarea in self.tareas: 
            print(f"Descripción: {tarea.descripcion} - Estado: {tarea.estado}")