##############################################################
from random import randint
from platos import Comestible, Bebestible

## Si necesita agregar imports, debe agregarlos aquí arriba ##

### INICIO PARTE 2.1 ###
class Persona:
    def __init__(self,n):
        self.nombre=str(n)
### FIN PARTE 2.1 ###

### INICIO PARTE 2.2 ###
class Repartidor(Persona):
    def __init__(self, n,t):
        super().__init__(n)
        if t>=20 and t<=30:
            self.tiempo_entrega=int(t)
        self.energia=randint(75,100)
    def repartir(self,pedido):
        if len(pedido)==0:
            return
        elif len(pedido)<=2:
            factor_tamano=5
            self.energia-=factor_tamano
            factor_velocidad=1.25
            tiempo_demora=self.tiempo_entrega*factor_velocidad
            return(tiempo_demora)
        elif len(pedido)>2:
            factor_factor=15
            self.energia-=factor_factor
            factor_velocidad=0.85
            tiempo_demora=self.tiempo_entrega*factor_velocidad
            return(tiempo_demora)
        print(f"El repartidor {self.nombre} se ha demorado {tiempo_demora} perdiendo {self.energia} de energía")
### FIN PARTE 2.2 ###

### INICIO PARTE 2.3 ###
class Cocinero(Persona):
    def __init__(self, n,h):
        super().__init__(n)
        if h>=1 and h<=10:
            self.habilidad=int(h)
        self.energia=randint(50,80)
    
    def cocinar(self,informacion_plato):
        if len(informacion_plato)==2:
            if informacion_plato[1]=="Bebestible":
                p=Bebestible(informacion_plato)
                if p.tamano=="pequeño":
                    self.energia-=5
                elif p.tamano=="medio":
                    self.energia-=8
                elif p.tamano=="grande":
                    self.energia-=10
            elif informacion_plato[1]=="Comestible":
                p=Comestible(informacion_plato)
                self.energia-=15
            if p.dificultad>self.habilidad:
                factor_calidad=0.7
                p.calidad=p.calidad*factor_calidad                
            elif p.dificultad<=self.habilidad:
                factor_calidad=1.5
                p.calidad=p.calidad*factor_calidad                
            print( f"El cocinero {self.nombre} ha cocinado {informacion_plato[0]} perdiendo {self.energia} de energia")
            return(p)
### FIN PARTE 2.3 ###

### INICIO PARTE 2.4 ###
class Cliente(Persona):
    def __init__(self, n, p):
        super().__init__(n)
        self.platos_preferidos = p
        
    def recibir_pedido(self, pedido, demora):
        calificacion=10
        if len(self.platos_preferidos)<len(pedido) or int(demora)>=20:
            calificacion=calificacion*0.5
            for plato in pedido:
                if plato.calidad>=11:
                    calificacion+=1.5
                elif plato.calidad<=8:
                    calificacion-=3
        print (f"El cliente {self.nombre} ha recibido su pedido y le puso la calificación {calificacion}")
        return(calificacion)

        ### FIN PARTE 2.4 ###

if __name__ == "__main__":

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        PLATOS_PRUEBA = {
        "Jugo Natural": ["Jugo Natural", "Bebestible"],
        "Empanadas": ["Empanadas", "Comestible"],
        }
        un_cocinero = Cocinero("Cristian", randint(1, 10))
        un_repartidor = Repartidor("Tomás", randint(20, 30))
        un_cliente = Cliente("Alberto", PLATOS_PRUEBA)
        print(f"El cocinero {un_cocinero.nombre} tiene una habilidad: {un_cocinero.habilidad}")
        print(f"El repatidor {un_repartidor.nombre} tiene una tiempo de entrega: {un_repartidor.tiempo_entrega} seg")
        print(f"El cliente {un_cliente.nombre} tiene los siguientes platos favoritos:")
        for plato in un_cliente.platos_preferidos.values():
            print(f" - {plato[1]}: {plato[0]}")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")